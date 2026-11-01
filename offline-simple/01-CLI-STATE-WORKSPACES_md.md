# Terraform explained in everyday language: 01-CLI-STATE-WORKSPACES.md

**Offline reference.** Use the command explanations to understand exactly what Terraform will inspect or change. Confirm the cloud account, backend, workspace, provider versions and saved plan before touching production. Original [guide](../01-CLI-STATE-WORKSPACES.md).

## 1. terraform version

```bash
terraform version
```

**Simply explained:** Shows the installed Terraform CLI release and provider versions.

**Command syntax:** `terraform version` identifies the tool and action. Other words are target resource addresses, paths or values.

**What should happen:** Terraform version number and information about available updates.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

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

## 5. terraform plan -out=tfplan

```bash
terraform plan -out=tfplan
```

**Simply explained:** Compares desired HCL with real resources and Terraform state, then calculates a proposed change.

**Command syntax:** `terraform plan` identifies the tool and action. Options: `-out=tfplan` = a tool-specific option (verify with terraform plan -help).

**What should happen:** A plan with resources to add, change and destroy. It can include sensitive details.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 6. terraform show tfplan

```bash
terraform show tfplan
```

**Simply explained:** Prints a saved plan or current state in readable or JSON form.

**Command syntax:** `terraform show` identifies the tool and action. Other words are target resource addresses, paths or values.

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

## 8. terraform output

```bash
terraform output
```

**Simply explained:** Reads outputs saved by Terraform after a successful apply.

**Command syntax:** `terraform output` identifies the tool and action. Other words are target resource addresses, paths or values.

**What should happen:** Output variable values, some of which may be confidential.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 9. terraform state list

```bash
terraform state list
```

**Simply explained:** Reads or manipulates Terraform state. `list`/`show` are diagnostic; `rm`/`mv` change mapping.

**Command syntax:** `terraform state` identifies the tool and action. Other words are target resource addresses, paths or values.

**What should happen:** Tracked resource addresses or current state changes, depending on subcommand.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 10. terraform state show 'module.example.aws_instance.node'

```bash
terraform state show 'module.example.aws_instance.node'
```

**Simply explained:** Reads or manipulates Terraform state. `list`/`show` are diagnostic; `rm`/`mv` change mapping.

**Command syntax:** `terraform state` identifies the tool and action. Other words are target resource addresses, paths or values.

**What should happen:** Tracked resource addresses or current state changes, depending on subcommand.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 11. terraform providers

```bash
terraform providers
```

**Simply explained:** Shows which provider plugins/modules are needed and selected.

**Command syntax:** `terraform providers` identifies the tool and action. Other words are target resource addresses, paths or values.

**What should happen:** Provider tree and version constraints.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 12. terraform output -json

```bash
terraform output -json
```

**Simply explained:** Reads outputs saved by Terraform after a successful apply.

**Command syntax:** `terraform output` identifies the tool and action. Options: `-json` = print machine-readable JSON, potentially confidential.

**What should happen:** Output variable values, some of which may be confidential.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 13. terraform show -json tfplan

```bash
terraform show -json tfplan
```

**Simply explained:** Prints a saved plan or current state in readable or JSON form.

**Command syntax:** `terraform show` identifies the tool and action. Options: `-json` = print machine-readable JSON, potentially confidential.

**What should happen:** Planned resource changes or state attributes, potentially sensitive.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 14. terraform init -upgrade

```bash
terraform init -upgrade
```

**Simply explained:** Prepares a Terraform working directory: downloads providers/modules and configures backend/state access.

**Command syntax:** `terraform init` identifies the tool and action. Options: `-upgrade` = allow downloading newer compatible provider/module versions.

**What should happen:** Initialization success, provider downloads, and possibly backend configuration prompts.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 15. terraform providers lock -platform=linux_amd64 -platform=darwin_arm64

```bash
terraform providers lock -platform=linux_amd64 -platform=darwin_arm64
```

**Simply explained:** Shows which provider plugins/modules are needed and selected.

**Command syntax:** `terraform providers` identifies the tool and action. Options: `-platform=linux_amd64` = a tool-specific option (verify with terraform providers -help); `-platform=darwin_arm64` = a tool-specific option (verify with terraform providers -help).

**What should happen:** Provider tree and version constraints.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 16. terraform get -update

```bash
terraform get -update
```

**Simply explained:** Downloads or updates referenced Terraform modules.

**Command syntax:** `terraform get` identifies the tool and action. Options: `-update` = a tool-specific option (verify with terraform get -help).

**What should happen:** Module initialization/download results.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 17. terraform plan -refresh-only

```bash
terraform plan -refresh-only
```

**Simply explained:** Compares desired HCL with real resources and Terraform state, then calculates a proposed change.

**Command syntax:** `terraform plan` identifies the tool and action. Options: `-refresh-only` = report or reconcile external drift rather than usual config edits.

**What should happen:** A plan with resources to add, change and destroy. It can include sensitive details.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 18. terraform import 'aws_instance.example' 'i-EXAMPLE'

```bash
terraform import 'aws_instance.example' 'i-EXAMPLE'
```

**Simply explained:** Tells Terraform to start tracking an existing real resource under a declared resource address.

**Command syntax:** `terraform import` identifies the tool and action. Other words are target resource addresses, paths or values.

**What should happen:** Successful import confirmation and new state mapping; no infrastructure is created.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** ⚠️ This can change cloud resources or Terraform state. Inspect a reviewed plan and backup state; reversing code does not guarantee rollback.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 19. terraform workspace list

```bash
terraform workspace list
```

**Simply explained:** Shows, creates or selects a named Terraform state workspace.

**Command syntax:** `terraform workspace` identifies the tool and action. Other words are target resource addresses, paths or values.

**What should happen:** Workspace list or selected workspace name.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 20. terraform workspace show

```bash
terraform workspace show
```

**Simply explained:** Shows, creates or selects a named Terraform state workspace.

**Command syntax:** `terraform workspace` identifies the tool and action. Other words are target resource addresses, paths or values.

**What should happen:** Workspace list or selected workspace name.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 21. terraform state pull

```bash
terraform state pull
```

**Simply explained:** Reads or manipulates Terraform state. `list`/`show` are diagnostic; `rm`/`mv` change mapping.

**Command syntax:** `terraform state` identifies the tool and action. Other words are target resource addresses, paths or values.

**What should happen:** Tracked resource addresses or current state changes, depending on subcommand.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** Usually reads/configures local Terraform or prepares a plan; protect plans and state because they may contain secrets.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 22. terraform state mv 'aws_instance.old' 'aws_instance.new'

```bash
terraform state mv 'aws_instance.old' 'aws_instance.new'
```

**Simply explained:** Reads or manipulates Terraform state. `list`/`show` are diagnostic; `rm`/`mv` change mapping.

**Command syntax:** `terraform state` identifies the tool and action. Other words are target resource addresses, paths or values.

**What should happen:** Tracked resource addresses or current state changes, depending on subcommand.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** ⚠️ This can change cloud resources or Terraform state. Inspect a reviewed plan and backup state; reversing code does not guarantee rollback.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

## 23. terraform state rm 'aws_instance.retired'

```bash
terraform state rm 'aws_instance.retired'
```

**Simply explained:** Reads or manipulates Terraform state. `list`/`show` are diagnostic; `rm`/`mv` change mapping.

**Command syntax:** `terraform state` identifies the tool and action. Other words are target resource addresses, paths or values.

**What should happen:** Tracked resource addresses or current state changes, depending on subcommand.

**Important inputs:** Check your environment, current state backend and workspace even without placeholders.

**Safety:** ⚠️ This can change cloud resources or Terraform state. Inspect a reviewed plan and backup state; reversing code does not guarantee rollback.

**If it fails:** Check provider/schema compatibility, missing variables, IAM permissions, API quotas and state-lock errors. Never use `-lock=false` simply to bypass another deployment.

