# AWS EKS starter. Requires PRE-EXISTING private subnets across >=2 AZs, VPC DNS/NAT,
# secure Terraform remote state and access to the private API through customer VPN/bastion.
terraform {
  required_version = ">= 1.8.0"
  required_providers {
    aws = { source = "hashicorp/aws", version = ">= 5.0, < 7.0" }
  }
}
provider "aws" { region = var.region }
variable "region" { type = string }
variable "cluster_name" { type = string }
variable "subnet_ids" {
  type = list(string)
  validation {
    condition = length(var.subnet_ids) >= 2
    error_message = "Specify >=2 private subnets in different AZs."
  }
}
variable "kubernetes_version" { type = string }
variable "node_instance_types" {
  type = list(string)
  default = ["m6i.large"]
}
data "aws_caller_identity" "current" {}
data "aws_iam_policy_document" "eks_assume" {
  statement {
    actions = ["sts:AssumeRole"]
    principals {
      type = "Service"
      identifiers = ["eks.amazonaws.com"]
    }
  }
}
data "aws_iam_policy_document" "node_assume" {
  statement {
    actions = ["sts:AssumeRole"]
    principals {
      type = "Service"
      identifiers = ["ec2.amazonaws.com"]
    }
  }
}
resource "aws_iam_role" "cluster" {
  name_prefix = "${var.cluster_name}-control-"
  assume_role_policy = data.aws_iam_policy_document.eks_assume.json
}
resource "aws_iam_role_policy_attachment" "cluster" {
  role = aws_iam_role.cluster.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
}
resource "aws_iam_role" "node" {
  name_prefix = "${var.cluster_name}-nodes-"
  assume_role_policy = data.aws_iam_policy_document.node_assume.json
}
resource "aws_iam_role_policy_attachment" "worker" {
  role = aws_iam_role.node.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy"
}
resource "aws_iam_role_policy_attachment" "registry" {
  role = aws_iam_role.node.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryPullOnly"
}
resource "aws_eks_cluster" "this" {
  name     = var.cluster_name
  role_arn = aws_iam_role.cluster.arn
  version  = var.kubernetes_version
  vpc_config {
    subnet_ids = var.subnet_ids
    endpoint_private_access = true
    endpoint_public_access  = false
  }
  enabled_cluster_log_types = ["api", "audit", "authenticator", "controllerManager", "scheduler"]
  access_config { authentication_mode = "API_AND_CONFIG_MAP" }
  depends_on = [aws_iam_role_policy_attachment.cluster]
}
resource "aws_eks_addon" "vpc_cni" {
  cluster_name = aws_eks_cluster.this.name
  addon_name = "vpc-cni"
}
resource "aws_eks_addon" "coredns" {
  cluster_name = aws_eks_cluster.this.name
  addon_name = "coredns"
}
resource "aws_eks_addon" "kube_proxy" {
  cluster_name = aws_eks_cluster.this.name
  addon_name = "kube-proxy"
}
resource "aws_eks_node_group" "workers" {
  cluster_name = aws_eks_cluster.this.name
  node_group_name = "general"
  node_role_arn = aws_iam_role.node.arn
  subnet_ids = var.subnet_ids
  instance_types = var.node_instance_types
  scaling_config {
    desired_size = 3
    min_size = 3
    max_size = 6
  }
  update_config { max_unavailable = 1 }
  depends_on = [aws_iam_role_policy_attachment.worker, aws_iam_role_policy_attachment.registry]
}
output "cluster_name" { value = aws_eks_cluster.this.name }
output "cluster_endpoint" { value = aws_eks_cluster.this.endpoint }
