# Offline command / configuration reference: `05-GITLAB-TERRAFORM-PIPELINE.md`

Generated from repository source by `tools/build_offline_reference.py`. **42 items**. This copy works offline. No commands were executed.

⚠️ **Version-aware reference, not a substitute for vendor docs.** Every individual command is preserved with purpose, flags, placeholders, expected output and risk. Ambiguous flags are marked as command-specific. Always verify flags against your installed CLI.

**Original file:** [`05-GITLAB-TERRAFORM-PIPELINE.md`](../05-GITLAB-TERRAFORM-PIPELINE.md)

### 1. Configuration field stages

**Source line:** 8. **Language:** yaml. **Full syntax:** stages = [validate, plan, deploy]

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 2. Configuration field variables

**Source line:** 9. **Language:** yaml. **Full syntax:** variables = 

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 3. Configuration field TF_IN_AUTOMATION

**Source line:** 10. **Language:** yaml. **Full syntax:** TF_IN_AUTOMATION = "true"

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 4. Configuration field TF_INPUT

**Source line:** 11. **Language:** yaml. **Full syntax:** TF_INPUT = "false"

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 5. Configuration field TF_ROOT

**Source line:** 12. **Language:** yaml. **Full syntax:** TF_ROOT = "templates/cloud-managed/aws-eks"

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 6. Configuration field TF_CLI_CONFIG_FILE

**Source line:** 13. **Language:** yaml. **Full syntax:** TF_CLI_CONFIG_FILE = "$CI_PROJECT_DIR/.terraformrc"

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 7. Configuration field validate

**Source line:** 15. **Language:** yaml. **Full syntax:** validate = 

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 8. Configuration field stage

**Source line:** 16. **Language:** yaml. **Full syntax:** stage = validate

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 9. Configuration field image

**Source line:** 17. **Language:** yaml. **Full syntax:** image = hashicorp/terraform:1.13

**What it does:** Container image; pin trusted registry and tested digest.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 10. Configuration field script

**Source line:** 18. **Language:** yaml. **Full syntax:** script = 

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 11. Configuration field rules

**Source line:** 23. **Language:** yaml. **Full syntax:** rules = 

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 12. Configuration field if

**Source line:** 24. **Language:** yaml. **Full syntax:** if = '$CI_PIPELINE_SOURCE == "merge_request_event"'

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 13. Configuration field if

**Source line:** 25. **Language:** yaml. **Full syntax:** if = '$CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH'

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 14. Configuration field plan

**Source line:** 27. **Language:** yaml. **Full syntax:** plan = 

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 15. Configuration field stage

**Source line:** 28. **Language:** yaml. **Full syntax:** stage = plan

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 16. Configuration field image

**Source line:** 29. **Language:** yaml. **Full syntax:** image = hashicorp/terraform:1.13

**What it does:** Container image; pin trusted registry and tested digest.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 17. Configuration field script

**Source line:** 30. **Language:** yaml. **Full syntax:** script = 

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 18. Configuration field artifacts

**Source line:** 34. **Language:** yaml. **Full syntax:** artifacts = 

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 19. Configuration field access

**Source line:** 35. **Language:** yaml. **Full syntax:** access = maintainer

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 20. Configuration field expire_in

**Source line:** 36. **Language:** yaml. **Full syntax:** expire_in = 1 day

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 21. Configuration field paths

**Source line:** 37. **Language:** yaml. **Full syntax:** paths = 

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 22. Configuration field rules

**Source line:** 39. **Language:** yaml. **Full syntax:** rules = 

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 23. Configuration field if

**Source line:** 40. **Language:** yaml. **Full syntax:** if = '$CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH'

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 24. Configuration field apply

**Source line:** 42. **Language:** yaml. **Full syntax:** apply = 

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 25. Configuration field stage

**Source line:** 43. **Language:** yaml. **Full syntax:** stage = deploy

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 26. Configuration field image

**Source line:** 44. **Language:** yaml. **Full syntax:** image = hashicorp/terraform:1.13

**What it does:** Container image; pin trusted registry and tested digest.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 27. Configuration field needs

**Source line:** 45. **Language:** yaml. **Full syntax:** needs = 

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 28. Configuration field job

**Source line:** 46. **Language:** yaml. **Full syntax:** job = plan

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 29. Configuration field artifacts

**Source line:** 47. **Language:** yaml. **Full syntax:** artifacts = true

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 30. Configuration field script

**Source line:** 48. **Language:** yaml. **Full syntax:** script = 

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 31. Configuration field resource_group

**Source line:** 52. **Language:** yaml. **Full syntax:** resource_group = production-infrastructure

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 32. Configuration field environment

**Source line:** 53. **Language:** yaml. **Full syntax:** environment = 

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 33. Configuration field name

**Source line:** 54. **Language:** yaml. **Full syntax:** name = production

**What it does:** Resource/cluster/host identity in the enclosing object.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 34. Configuration field when

**Source line:** 55. **Language:** yaml. **Full syntax:** when = manual

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 35. Configuration field rules

**Source line:** 56. **Language:** yaml. **Full syntax:** rules = 

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 36. Configuration field if

**Source line:** 57. **Language:** yaml. **Full syntax:** if = '$CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH'

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 37. `terraform fmt -check -recursive`

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

### 38. `terraform init`

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

### 39. `terraform validate`

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

### 40. `terraform plan -lock-timeout=5m -out=tfplan`

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

### 41. `terraform show -no-color tfplan`

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

### 42. `terraform apply tfplan`

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

