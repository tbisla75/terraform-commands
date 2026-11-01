# Terraform explained in everyday language: 05-GITLAB-TERRAFORM-PIPELINE.md

**Offline reference.** Use the command explanations to understand exactly what Terraform will inspect or change. Confirm the cloud account, backend, workspace, provider versions and saved plan before touching production. Original [guide](../05-GITLAB-TERRAFORM-PIPELINE.md).

## 1. Configuration

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

**In simple terms:** This block configures a pipeline or Terraform setting. It does not change a cloud resource until a pipeline step/terraform apply runs. Review permissions, credentials, state storage and which environment is targeted.

## 2. terraform fmt -check -recursive

```bash
terraform fmt -check -recursive
```

**Simply explained:** Checks or rewrites Terraform file formatting. With `-check`, it reports differences without changing files.

**Command syntax:** `terraform fmt` identifies the tool and action. Options: `-check` = check formatting only, do not rewrite files; `-recursive` = include nested module directories.

**What should happen:** Names of incorrectly formatted files or no output if formatting is valid.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 3. terraform init

```bash
terraform init
```

**Simply explained:** Prepares a Terraform working directory: downloads providers/modules and configures backend/state access.

**Command syntax:** `terraform init` identifies the tool and action. Other words are target resource addresses, paths or values.

**What should happen:** Initialization success, provider downloads, and possibly backend configuration prompts.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 4. terraform validate

```bash
terraform validate
```

**Simply explained:** Checks whether Terraform HCL configuration is internally valid. It does not prove cloud permissions or quotas.

**Command syntax:** `terraform validate` identifies the tool and action. Other words are target resource addresses, paths or values.

**What should happen:** `Success! The configuration is valid` or exact validation errors.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 5. terraform plan -lock-timeout=5m -out=tfplan

```bash
terraform plan -lock-timeout=5m -out=tfplan
```

**Simply explained:** Compares desired HCL with real resources and Terraform state, then calculates a proposed change.

**Command syntax:** `terraform plan` identifies the tool and action. Options: `-lock-timeout=5m` = a tool-specific option (verify with terraform plan -help); `-out=tfplan` = a tool-specific option (verify with terraform plan -help).

**What should happen:** A plan with resources to add, change and destroy. It can include sensitive details.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 6. terraform show -no-color tfplan

```bash
terraform show -no-color tfplan
```

**Simply explained:** Prints a saved plan or current state in readable or JSON form.

**Command syntax:** `terraform show` identifies the tool and action. Options: `-no-color` = remove terminal color escape codes.

**What should happen:** Planned resource changes or state attributes, potentially sensitive.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 7. terraform apply tfplan

```bash
terraform apply tfplan
```

**Simply explained:** Executes the approved plan against real infrastructure. This changes cloud resources and state.

**Command syntax:** `terraform apply` identifies the tool and action. Other words are target resource addresses, paths or values.

**What should happen:** Resource creation/update/deletion progress followed by an apply summary.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** ⚠️ This can change cloud resources or Terraform state. Inspect a reviewed plan and backup state; reversing code does not guarantee rollback.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

