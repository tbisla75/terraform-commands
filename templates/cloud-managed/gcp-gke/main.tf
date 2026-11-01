# GKE Standard private-node cluster, existing network+subnetwork+Cloud NAT/DNS required.
terraform {
  required_version = ">= 1.8.0"
  required_providers {
    google = { source = "hashicorp/google", version = ">= 5.0, < 8.0" }
  }
}
provider "google" { project = var.project_id region = var.region }
variable "project_id" { type = string }
variable "region" { type = string }
variable "cluster_name" { type = string }
variable "network" { type = string }
variable "subnetwork" { type = string }
variable "pods_secondary_range_name" { type = string }
variable "services_secondary_range_name" { type = string }
variable "release_channel" {
  type = string
  default = "REGULAR"
}
variable "authorized_admin_cidrs" { type = list(string) }
resource "google_container_cluster" "this" {
  name = var.cluster_name
  location = var.region
  network = var.network
  subnetwork = var.subnetwork
  remove_default_node_pool = true
  initial_node_count = 1
  release_channel { channel = var.release_channel }
  ip_allocation_policy {
    cluster_secondary_range_name = var.pods_secondary_range_name
    services_secondary_range_name = var.services_secondary_range_name
  }
  private_cluster_config {
    enable_private_nodes = true
    enable_private_endpoint = false
    master_ipv4_cidr_block = "172.16.0.0/28" # must not overlap VPC/on-prem routes
  }
  master_authorized_networks_config {
    dynamic "cidr_blocks" {
      for_each = var.authorized_admin_cidrs
      content {
        cidr_block   = cidr_blocks.value
        display_name = "approved-administrator"
      }
    }
  }
  workload_identity_config {
    workload_pool = "${var.project_id}.svc.id.goog"
  }
  logging_service = "logging.googleapis.com/kubernetes"
  monitoring_service = "monitoring.googleapis.com/kubernetes"
  deletion_protection = true
}
resource "google_container_node_pool" "apps" {
  name = "apps"
  cluster = google_container_cluster.this.name
  location = var.region
  node_count = 1 # per zone; 3 regional zones => 3 total nodes
  management { auto_repair = true auto_upgrade = true }
  node_config {
    machine_type = "e2-standard-4"
    oauth_scopes = ["https://www.googleapis.com/auth/cloud-platform"]
    workload_metadata_config { mode = "GKE_METADATA" }
    shielded_instance_config { enable_secure_boot = true enable_integrity_monitoring = true }
  }
}
output "cluster_name" { value = google_container_cluster.this.name }
