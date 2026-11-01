# Offline command / configuration reference: `05-GITLAB-TERRAFORM-PIPELINE.md`

Generated from repository source by `tools/build_offline_reference.py`. **7 items**. This copy works offline. No commands were executed.

⚠️ **Version-aware reference, not a substitute for vendor docs.** Every individual command is preserved with purpose, flags, placeholders, expected output and risk. Ambiguous flags are marked as command-specific. Always verify flags against your installed CLI.

**Original file:** [`05-GITLAB-TERRAFORM-PIPELINE.md`](../05-GITLAB-TERRAFORM-PIPELINE.md)

### 1. Configuration example (yaml)

**Source line:** 8. **Purpose:** Define declarative settings, not a standalone CLI command. Review image references, identity, network addresses, permissions and secrets.

```yaml
stages: [validate, plan, deploy]
variables:
  TF_IN_AUTOMATION: "true"
  TF_INPUT: "false"
  TF_ROOT: "templates/cloud-managed/aws-eks"
  TF_CLI_CONFIG_FILE: "$CI_PROJECT_DIR/.terraformrc"

validate:
  stage: validate
  image: hashicorp/terraform:1.13
  script:
    - cd "$TF_ROOT"
    - terraform fmt -check -recursive
    - terraform init -backend=false
    - terraform validate
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
    - if: '$CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH'

plan:
  stage: plan
  image: hashicorp/terraform:1.13
  script:
    - cd "$TF_ROOT"
    - terraform init -lock-timeout=5m
    - terraform plan -lock-timeout=5m -out=tfplan
  artifacts:
    access: maintainer
    expire_in: 1 day
    paths:
      - "$TF_ROOT/tfplan"
  rules:
    - if: '$CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH'

apply:
  stage: deploy
  image: hashicorp/terraform:1.13
  needs:
    - job: plan
      artifacts: true
  script:
    - cd "$TF_ROOT"
    - terraform init -lock-timeout=5m
    - terraform apply -lock-timeout=5m tfplan
  resource_group: production-infrastructure
  environment:
    name: production
  when: manual
  rules:
    - if: '$CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH'
```

**Syntax:** YAML/HCL keys and indentation map to release-specific APIs. **Safety:** Applying may change live infrastructure; validate schema, diff and recovery first.

### 2. `terraform fmt -check -recursive`

**Source line:** 65  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform fmt -check -recursive
```

**What it does:** Format Terraform config files (unless check-only mode).

**Syntax:** terraform fmt -check -recursive. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Option:** `-check` — Command-specific option or abbreviated argument; verify with installed CLI help and vendor reference.
**Option:** `-recursive` — Command-specific option or abbreviated argument; verify with installed CLI help and vendor reference.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Format Terraform config files (unless check-only mode). Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 3. `terraform init`

**Source line:** 66  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform init
```

**What it does:** Download/setup providers/modules and initialize backend; changes local working files.

**Syntax:** terraform init. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Download/setup providers/modules and initialize backend; changes local working files. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 4. `terraform validate`

**Source line:** 67  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform validate
```

**What it does:** Check Terraform configuration syntax and type/schema consistency.

**Syntax:** terraform validate. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Check Terraform configuration syntax and type/schema consistency. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 5. `terraform plan -lock-timeout=5m -out=tfplan`

**Source line:** 68  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform plan -lock-timeout=5m -out=tfplan
```

**What it does:** Compute proposed infrastructure change plan (typically does not mutate managed infrastructure).

**Syntax:** terraform plan -lock-timeout=5m -out=tfplan. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Option:** `-lock-timeout=5m` — Command-specific option or abbreviated argument; verify with installed CLI help and vendor reference.
**Option:** `-out=tfplan` — Command-specific option or abbreviated argument; verify with installed CLI help and vendor reference.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Compute proposed infrastructure change plan (typically does not mutate managed infrastructure). Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 6. `terraform show -no-color tfplan`

**Source line:** 69  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform show -no-color tfplan
```

**What it does:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive.

**Syntax:** terraform show -no-color tfplan. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Option:** `-no-color` — Command-specific option or abbreviated argument; verify with installed CLI help and vendor reference.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 7. `terraform apply tfplan`

**Source line:** 70  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **CHANGE / POSSIBLY MUTATING**

**Exact command:**

```bash
terraform apply tfplan
```

**What it does:** Apply proposed changes to real infrastructure and Terraform state.

**Syntax:** terraform apply tfplan. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Safety/rollback:** Check subcommand and flags; requires change review and appropriate access.
**Expected result:** Apply proposed changes to real infrastructure and Terraform state. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

