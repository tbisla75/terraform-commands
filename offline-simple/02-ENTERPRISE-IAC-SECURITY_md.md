# Terraform explained in everyday language: 02-ENTERPRISE-IAC-SECURITY.md

**Offline reference.** Use the command explanations to understand exactly what Terraform will inspect or change. Confirm the cloud account, backend, workspace, provider versions and saved plan before touching production. Original [guide](../02-ENTERPRISE-IAC-SECURITY.md).

## 1. terraform fmt -check -recursive

```bash
terraform fmt -check -recursive
```

**Simply explained:** Checks or rewrites Terraform file formatting. With `-check`, it reports differences without changing files.

**Command syntax:** `terraform fmt` identifies the tool and action. Options: `-check` = check formatting only, do not rewrite files; `-recursive` = include nested module directories.

**What should happen:** Names of incorrectly formatted files or no output if formatting is valid.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 2. terraform init -backend=false

```bash
terraform init -backend=false
```

**Simply explained:** Prepares a Terraform working directory: downloads providers/modules and configures backend/state access.

**Command syntax:** `terraform init` identifies the tool and action. Options: `-backend=false` = a tool-specific option (verify with terraform init -help).

**What should happen:** Initialization success, provider downloads, and possibly backend configuration prompts.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 3. terraform validate

```bash
terraform validate
```

**Simply explained:** Checks whether Terraform HCL configuration is internally valid. It does not prove cloud permissions or quotas.

**Command syntax:** `terraform validate` identifies the tool and action. Other words are target resource addresses, paths or values.

**What should happen:** `Success! The configuration is valid` or exact validation errors.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 4. terraform plan -lock-timeout=5m -out=tfplan

```bash
terraform plan -lock-timeout=5m -out=tfplan
```

**Simply explained:** Compares desired HCL with real resources and Terraform state, then calculates a proposed change.

**Command syntax:** `terraform plan` identifies the tool and action. Options: `-lock-timeout=5m` = a tool-specific option (verify with terraform plan -help); `-out=tfplan` = a tool-specific option (verify with terraform plan -help).

**What should happen:** A plan with resources to add, change and destroy. It can include sensitive details.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 5. terraform show -no-color tfplan

```bash
terraform show -no-color tfplan
```

**Simply explained:** Prints a saved plan or current state in readable or JSON form.

**Command syntax:** `terraform show` identifies the tool and action. Options: `-no-color` = remove terminal color escape codes.

**What should happen:** Planned resource changes or state attributes, potentially sensitive.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 6. trivy config .

```bash
trivy config .
```

**Simply explained:** This runs an infrastructure/shell tool; use its arguments to choose target files or cloud resources.

**Command syntax:** `trivy config` identifies the tool and action. Other words are target resource addresses, paths or values.

**What should happen:** The relevant tool's status and error messages.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 7. checkov -d .

```bash
checkov -d .
```

**Simply explained:** This runs an infrastructure/shell tool; use its arguments to choose target files or cloud resources.

**Command syntax:** `checkov -d` identifies the tool and action. Options: `-d` = a tool-specific option (verify with terraform  -help).

**What should happen:** The relevant tool's status and error messages.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 8. tflint --init

```bash
tflint --init
```

**Simply explained:** This runs an infrastructure/shell tool; use its arguments to choose target files or cloud resources.

**Command syntax:** `tflint --init` identifies the tool and action. Options: `--init` = a tool-specific option (verify with terraform  -help).

**What should happen:** The relevant tool's status and error messages.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 9. tflint --recursive

```bash
tflint --recursive
```

**Simply explained:** This runs an infrastructure/shell tool; use its arguments to choose target files or cloud resources.

**Command syntax:** `tflint --recursive` identifies the tool and action. Options: `--recursive` = a tool-specific option (verify with terraform  -help).

**What should happen:** The relevant tool's status and error messages.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 10. terraform providers

```bash
terraform providers
```

**Simply explained:** Shows which provider plugins/modules are needed and selected.

**Command syntax:** `terraform providers` identifies the tool and action. Other words are target resource addresses, paths or values.

**What should happen:** Provider tree and version constraints.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 11. terraform providers lock -platform=linux_amd64

```bash
terraform providers lock -platform=linux_amd64
```

**Simply explained:** Shows which provider plugins/modules are needed and selected.

**Command syntax:** `terraform providers` identifies the tool and action. Options: `-platform=linux_amd64` = a tool-specific option (verify with terraform providers -help).

**What should happen:** Provider tree and version constraints.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 12. terraform plan -refresh-only

```bash
terraform plan -refresh-only
```

**Simply explained:** Compares desired HCL with real resources and Terraform state, then calculates a proposed change.

**Command syntax:** `terraform plan` identifies the tool and action. Options: `-refresh-only` = report or reconcile external drift rather than usual config edits.

**What should happen:** A plan with resources to add, change and destroy. It can include sensitive details.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 13. terraform state list

```bash
terraform state list
```

**Simply explained:** Reads or manipulates Terraform state. `list`/`show` are diagnostic; `rm`/`mv` change mapping.

**Command syntax:** `terraform state` identifies the tool and action. Other words are target resource addresses, paths or values.

**What should happen:** Tracked resource addresses or current state changes, depending on subcommand.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 14. terraform providers

```bash
terraform providers
```

**Simply explained:** Shows which provider plugins/modules are needed and selected.

**Command syntax:** `terraform providers` identifies the tool and action. Other words are target resource addresses, paths or values.

**What should happen:** Provider tree and version constraints.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 15. terraform validate

```bash
terraform validate
```

**Simply explained:** Checks whether Terraform HCL configuration is internally valid. It does not prove cloud permissions or quotas.

**Command syntax:** `terraform validate` identifies the tool and action. Other words are target resource addresses, paths or values.

**What should happen:** `Success! The configuration is valid` or exact validation errors.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 16. terraform graph

```bash
terraform graph
```

**Simply explained:** Prints dependency graph (DOT format).

**Command syntax:** `terraform graph` identifies the tool and action. Other words are target resource addresses, paths or values.

**What should happen:** Text graph showing resource relationships.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

