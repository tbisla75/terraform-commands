# Azure AKS starter. Existing VNet subnet + private DNS/access, resource group and policies required.
terraform {
  required_version = ">= 1.8.0"
  required_providers {
    azurerm = { source = "hashicorp/azurerm", version = ">= 4.0, < 6.0" }
  }
}
provider "azurerm" { features {} subscription_id = var.subscription_id }
variable "subscription_id" { type = string }
variable "resource_group_name" { type = string }
variable "location" { type = string }
variable "cluster_name" { type = string }
variable "vnet_subnet_id" { type = string }
variable "kubernetes_version" { type = string }
variable "admin_group_object_ids" { type = list(string) }
data "azurerm_resource_group" "existing" { name = var.resource_group_name }
resource "azurerm_kubernetes_cluster" "this" {
  name = var.cluster_name
  location = var.location
  resource_group_name = data.azurerm_resource_group.existing.name
  dns_prefix = var.cluster_name
  kubernetes_version = var.kubernetes_version
  private_cluster_enabled = true
  local_account_disabled = true
  role_based_access_control_enabled = true
  sku_tier = "Standard"
  oidc_issuer_enabled = true
  workload_identity_enabled = true
  default_node_pool {
    name = "system"
    vm_size = "Standard_D4s_v5"
    node_count = 3
    vnet_subnet_id = var.vnet_subnet_id
    zones = ["1", "2", "3"]
    max_pods = 30
    only_critical_addons_enabled = true
    upgrade_settings { max_surge = "33%" }
  }
  identity { type = "SystemAssigned" }
  network_profile { network_plugin = "azure" network_plugin_mode = "overlay" }
  azure_active_directory_role_based_access_control {
    azure_rbac_enabled = true
    admin_group_object_ids = var.admin_group_object_ids
  }
}
resource "azurerm_kubernetes_cluster_node_pool" "apps" {
  name = "apps"
  kubernetes_cluster_id = azurerm_kubernetes_cluster.this.id
  vm_size = "Standard_D4s_v5"
  node_count = 3
  vnet_subnet_id = var.vnet_subnet_id
  zones = ["1", "2", "3"]
  mode = "User"
  upgrade_settings { max_surge = "33%" }
}
output "cluster_name" { value = azurerm_kubernetes_cluster.this.name }
