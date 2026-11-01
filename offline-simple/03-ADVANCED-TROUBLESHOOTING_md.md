# Terraform explained in everyday language: 03-ADVANCED-TROUBLESHOOTING.md

**Offline reference.** Use the command explanations to understand exactly what Terraform will inspect or change. Confirm the cloud account, backend, workspace, provider versions and saved plan before touching production. Original [guide](../03-ADVANCED-TROUBLESHOOTING.md).

## 1. terraform init -reconfigure

```bash
terraform init -reconfigure
```

**Simply explained:** Prepares a Terraform working directory: downloads providers/modules and configures backend/state access.

**Command syntax:** `terraform init` identifies the tool and action. Options: `-reconfigure` = reinitialize the backend without migrating state.

**What should happen:** Initialization success, provider downloads, and possibly backend configuration prompts.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 2. terraform providers

```bash
terraform providers
```

**Simply explained:** Shows which provider plugins/modules are needed and selected.

**Command syntax:** `terraform providers` identifies the tool and action. Other words are target resource addresses, paths or values.

**What should happen:** Provider tree and version constraints.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 3. terraform workspace show

```bash
terraform workspace show
```

**Simply explained:** Shows, creates or selects a named Terraform state workspace.

**Command syntax:** `terraform workspace` identifies the tool and action. Other words are target resource addresses, paths or values.

**What should happen:** Workspace list or selected workspace name.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 4. terraform plan -lock-timeout=10m

```bash
terraform plan -lock-timeout=10m
```

**Simply explained:** Compares desired HCL with real resources and Terraform state, then calculates a proposed change.

**Command syntax:** `terraform plan` identifies the tool and action. Options: `-lock-timeout=10m` = a tool-specific option (verify with terraform plan -help).

**What should happen:** A plan with resources to add, change and destroy. It can include sensitive details.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 5. terraform plan -refresh-only

```bash
terraform plan -refresh-only
```

**Simply explained:** Compares desired HCL with real resources and Terraform state, then calculates a proposed change.

**Command syntax:** `terraform plan` identifies the tool and action. Options: `-refresh-only` = report or reconcile external drift rather than usual config edits.

**What should happen:** A plan with resources to add, change and destroy. It can include sensitive details.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 6. terraform state list

```bash
terraform state list
```

**Simply explained:** Reads or manipulates Terraform state. `list`/`show` are diagnostic; `rm`/`mv` change mapping.

**Command syntax:** `terraform state` identifies the tool and action. Other words are target resource addresses, paths or values.

**What should happen:** Tracked resource addresses or current state changes, depending on subcommand.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 7. terraform plan -target='module.network'

```bash
terraform plan -target='module.network'
```

**Simply explained:** Compares desired HCL with real resources and Terraform state, then calculates a proposed change.

**Command syntax:** `terraform plan` identifies the tool and action. Options: `-target='module.network'` = limit evaluation to chosen resources (exceptional recovery, not normal deployment).

**What should happen:** A plan with resources to add, change and destroy. It can include sensitive details.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 8. terraform plan -replace='aws_instance.example'

```bash
terraform plan -replace='aws_instance.example'
```

**Simply explained:** Compares desired HCL with real resources and Terraform state, then calculates a proposed change.

**Command syntax:** `terraform plan` identifies the tool and action. Options: `-replace='aws_instance.example'` = force recreation of a specific resource; outage/data loss risk.

**What should happen:** A plan with resources to add, change and destroy. It can include sensitive details.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** ⚠️ This can change cloud resources or Terraform state. Inspect a reviewed plan and backup state; reversing code does not guarantee rollback.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 9. terraform import 'aws_instance.example' 'i-EXAMPLE'

```bash
terraform import 'aws_instance.example' 'i-EXAMPLE'
```

**Simply explained:** Tells Terraform to start tracking an existing real resource under a declared resource address.

**Command syntax:** `terraform import` identifies the tool and action. Other words are target resource addresses, paths or values.

**What should happen:** Successful import confirmation and new state mapping; no infrastructure is created.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** ⚠️ This can change cloud resources or Terraform state. Inspect a reviewed plan and backup state; reversing code does not guarantee rollback.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 10. terraform state show 'aws_instance.example'

```bash
terraform state show 'aws_instance.example'
```

**Simply explained:** Reads or manipulates Terraform state. `list`/`show` are diagnostic; `rm`/`mv` change mapping.

**Command syntax:** `terraform state` identifies the tool and action. Other words are target resource addresses, paths or values.

**What should happen:** Tracked resource addresses or current state changes, depending on subcommand.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 11. terraform version

```bash
terraform version
```

**Simply explained:** Shows the installed Terraform CLI release and provider versions.

**Command syntax:** `terraform version` identifies the tool and action. Other words are target resource addresses, paths or values.

**What should happen:** Terraform version number and information about available updates.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 12. terraform providers

```bash
terraform providers
```

**Simply explained:** Shows which provider plugins/modules are needed and selected.

**Command syntax:** `terraform providers` identifies the tool and action. Other words are target resource addresses, paths or values.

**What should happen:** Provider tree and version constraints.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 13. terraform validate

```bash
terraform validate
```

**Simply explained:** Checks whether Terraform HCL configuration is internally valid. It does not prove cloud permissions or quotas.

**Command syntax:** `terraform validate` identifies the tool and action. Other words are target resource addresses, paths or values.

**What should happen:** `Success! The configuration is valid` or exact validation errors.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 14. terraform console

```bash
terraform console
```

**Simply explained:** Starts an interactive evaluator for Terraform expressions.

**Command syntax:** `terraform console` identifies the tool and action. Other words are target resource addresses, paths or values.

**What should happen:** Expression results or prompt.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 15. terraform show -json tfplan

```bash
terraform show -json tfplan
```

**Simply explained:** Prints a saved plan or current state in readable or JSON form.

**Command syntax:** `terraform show` identifies the tool and action. Options: `-json` = print machine-readable JSON, potentially confidential.

**What should happen:** Planned resource changes or state attributes, potentially sensitive.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

