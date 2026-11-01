# OFFLINE TERRAFORM / IAC REFERENCE: 05-GITLAB-TERRAFORM-PIPELINE.md

Works locally without ChatGPT. Derived directly from [05-GITLAB-TERRAFORM-PIPELINE.md](../05-GITLAB-TERRAFORM-PIPELINE.md). Every available command includes syntax, state safety and intended output. Validate provider-specific options and release constraints before application.

## 1. yaml configuration

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

**Syntax:** Declarative field/value structure. Schema and evaluation depend on selected provider/application version. **State:** no cloud effect until apply/sync. Protect secrets and review desired changes before executing.

## 2. terraform fmt -check -recursive

```bash
terraform fmt -check -recursive
```

**Purpose:** Reformat/validate configuration formatting.

**Syntax:** `terraform` is the executable; `fmt` selects subcommand; trailing operands/flags choose target and behavior. `-check` = a CLI option; verify with installed help; `-recursive` = a CLI option; verify with installed help

**Expected output:** Reformat/validate configuration formatting. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 3. terraform init

```bash
terraform init
```

**Purpose:** Initialize provider modules and backend; downloads dependencies and may configure backend.

**Syntax:** `terraform` is the executable; `init` selects subcommand; trailing operands/flags choose target and behavior. No named options; inspect positional arguments.

**Expected output:** Initialize provider modules and backend; downloads dependencies and may configure backend. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 4. terraform validate

```bash
terraform validate
```

**Purpose:** Statically validate Terraform configuration/schema.

**Syntax:** `terraform` is the executable; `validate` selects subcommand; trailing operands/flags choose target and behavior. No named options; inspect positional arguments.

**Expected output:** Statically validate Terraform configuration/schema. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 5. terraform plan -lock-timeout=5m -out=tfplan

```bash
terraform plan -lock-timeout=5m -out=tfplan
```

**Purpose:** Calculate infrastructure changes and store optional sensitive plan file.

**Syntax:** `terraform` is the executable; `plan` selects subcommand; trailing operands/flags choose target and behavior. `-lock-timeout=5m` = a CLI option; verify with installed help; `-out=tfplan` = a CLI option; verify with installed help

**Expected output:** Calculate infrastructure changes and store optional sensitive plan file. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 6. terraform show -no-color tfplan

```bash
terraform show -no-color tfplan
```

**Purpose:** Display state or saved plan; may contain secrets.

**Syntax:** `terraform` is the executable; `show` selects subcommand; trailing operands/flags choose target and behavior. `-no-color` = a CLI option; verify with installed help

**Expected output:** Display state or saved plan; may contain secrets. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 7. terraform apply tfplan

```bash
terraform apply tfplan
```

**Purpose:** Reconcile real cloud resources and state; mutating.

**Syntax:** `terraform` is the executable; `apply` selects subcommand; trailing operands/flags choose target and behavior. No named options; inspect positional arguments.

**Expected output:** Reconcile real cloud resources and state; mutating. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🔴 Can mutate real cloud resources or state. Requires a reviewed plan and recovery strategy.

