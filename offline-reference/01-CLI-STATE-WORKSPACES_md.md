# OFFLINE TERRAFORM / IAC REFERENCE: 01-CLI-STATE-WORKSPACES.md

Works locally without ChatGPT. Derived directly from [01-CLI-STATE-WORKSPACES.md](../01-CLI-STATE-WORKSPACES.md). Every available command includes syntax, state safety and intended output. Validate provider-specific options and release constraints before application.

## 1. terraform version

```bash
terraform version
```

**Purpose:** Terraform CLI operation; check version-specific docs.

**Syntax:** `terraform` is the executable; `version` selects subcommand; trailing operands/flags choose target and behavior. No named options; inspect positional arguments.

**Expected output:** Terraform CLI operation; check version-specific docs. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

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

## 5. terraform plan -out=tfplan

```bash
terraform plan -out=tfplan
```

**Purpose:** Calculate infrastructure changes and store optional sensitive plan file.

**Syntax:** `terraform` is the executable; `plan` selects subcommand; trailing operands/flags choose target and behavior. `-out=tfplan` = a CLI option; verify with installed help

**Expected output:** Calculate infrastructure changes and store optional sensitive plan file. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 6. terraform show tfplan

```bash
terraform show tfplan
```

**Purpose:** Display state or saved plan; may contain secrets.

**Syntax:** `terraform` is the executable; `show` selects subcommand; trailing operands/flags choose target and behavior. No named options; inspect positional arguments.

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

## 8. terraform output

```bash
terraform output
```

**Purpose:** Display outputs, which can reveal sensitive values.

**Syntax:** `terraform` is the executable; `output` selects subcommand; trailing operands/flags choose target and behavior. No named options; inspect positional arguments.

**Expected output:** Display outputs, which can reveal sensitive values. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 9. terraform state list

```bash
terraform state list
```

**Purpose:** Inspect or rewrite Terraform state depending on subcommand; potentially high-risk.

**Syntax:** `terraform` is the executable; `state` selects subcommand; trailing operands/flags choose target and behavior. No named options; inspect positional arguments.

**Expected output:** Inspect or rewrite Terraform state depending on subcommand; potentially high-risk. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 10. terraform state show 'module.example.aws_instance.node'

```bash
terraform state show 'module.example.aws_instance.node'
```

**Purpose:** Inspect or rewrite Terraform state depending on subcommand; potentially high-risk.

**Syntax:** `terraform` is the executable; `state` selects subcommand; trailing operands/flags choose target and behavior. No named options; inspect positional arguments.

**Expected output:** Inspect or rewrite Terraform state depending on subcommand; potentially high-risk. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 11. terraform providers

```bash
terraform providers
```

**Purpose:** Inspect provider dependencies and lockfile constraints.

**Syntax:** `terraform` is the executable; `providers` selects subcommand; trailing operands/flags choose target and behavior. No named options; inspect positional arguments.

**Expected output:** Inspect provider dependencies and lockfile constraints. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 12. terraform output -json

```bash
terraform output -json
```

**Purpose:** Display outputs, which can reveal sensitive values.

**Syntax:** `terraform` is the executable; `output` selects subcommand; trailing operands/flags choose target and behavior. `-json` = a CLI option; verify with installed help

**Expected output:** Display outputs, which can reveal sensitive values. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 13. terraform show -json tfplan

```bash
terraform show -json tfplan
```

**Purpose:** Display state or saved plan; may contain secrets.

**Syntax:** `terraform` is the executable; `show` selects subcommand; trailing operands/flags choose target and behavior. `-json` = a CLI option; verify with installed help

**Expected output:** Display state or saved plan; may contain secrets. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 14. terraform init -upgrade

```bash
terraform init -upgrade
```

**Purpose:** Initialize provider modules and backend; downloads dependencies and may configure backend.

**Syntax:** `terraform` is the executable; `init` selects subcommand; trailing operands/flags choose target and behavior. `-upgrade` = a CLI option; verify with installed help

**Expected output:** Initialize provider modules and backend; downloads dependencies and may configure backend. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 15. terraform providers lock -platform=linux_amd64 -platform=darwin_arm64

```bash
terraform providers lock -platform=linux_amd64 -platform=darwin_arm64
```

**Purpose:** Inspect provider dependencies and lockfile constraints.

**Syntax:** `terraform` is the executable; `providers` selects subcommand; trailing operands/flags choose target and behavior. `-platform=linux_amd64` = a CLI option; verify with installed help; `-platform=darwin_arm64` = a CLI option; verify with installed help

**Expected output:** Inspect provider dependencies and lockfile constraints. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 16. terraform get -update

```bash
terraform get -update
```

**Purpose:** Terraform CLI operation; check version-specific docs.

**Syntax:** `terraform` is the executable; `get` selects subcommand; trailing operands/flags choose target and behavior. `-update` = a CLI option; verify with installed help

**Expected output:** Terraform CLI operation; check version-specific docs. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 17. terraform plan -refresh-only

```bash
terraform plan -refresh-only
```

**Purpose:** Calculate infrastructure changes and store optional sensitive plan file.

**Syntax:** `terraform` is the executable; `plan` selects subcommand; trailing operands/flags choose target and behavior. `-refresh-only` = a CLI option; verify with installed help

**Expected output:** Calculate infrastructure changes and store optional sensitive plan file. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 18. terraform import 'aws_instance.example' 'i-EXAMPLE'

```bash
terraform import 'aws_instance.example' 'i-EXAMPLE'
```

**Purpose:** Associate pre-existing infrastructure with Terraform state.

**Syntax:** `terraform` is the executable; `import` selects subcommand; trailing operands/flags choose target and behavior. No named options; inspect positional arguments.

**Expected output:** Associate pre-existing infrastructure with Terraform state. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🔴 Can mutate real cloud resources or state. Requires a reviewed plan and recovery strategy.

## 19. terraform workspace list

```bash
terraform workspace list
```

**Purpose:** Manage logical state selection and workspace metadata.

**Syntax:** `terraform` is the executable; `workspace` selects subcommand; trailing operands/flags choose target and behavior. No named options; inspect positional arguments.

**Expected output:** Manage logical state selection and workspace metadata. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 20. terraform workspace show

```bash
terraform workspace show
```

**Purpose:** Manage logical state selection and workspace metadata.

**Syntax:** `terraform` is the executable; `workspace` selects subcommand; trailing operands/flags choose target and behavior. No named options; inspect positional arguments.

**Expected output:** Manage logical state selection and workspace metadata. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 21. terraform state pull

```bash
terraform state pull
```

**Purpose:** Inspect or rewrite Terraform state depending on subcommand; potentially high-risk.

**Syntax:** `terraform` is the executable; `state` selects subcommand; trailing operands/flags choose target and behavior. No named options; inspect positional arguments.

**Expected output:** Inspect or rewrite Terraform state depending on subcommand; potentially high-risk. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 22. terraform state mv 'aws_instance.old' 'aws_instance.new'

```bash
terraform state mv 'aws_instance.old' 'aws_instance.new'
```

**Purpose:** Inspect or rewrite Terraform state depending on subcommand; potentially high-risk.

**Syntax:** `terraform` is the executable; `state` selects subcommand; trailing operands/flags choose target and behavior. No named options; inspect positional arguments.

**Expected output:** Inspect or rewrite Terraform state depending on subcommand; potentially high-risk. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🔴 Can mutate real cloud resources or state. Requires a reviewed plan and recovery strategy.

## 23. terraform state rm 'aws_instance.retired'

```bash
terraform state rm 'aws_instance.retired'
```

**Purpose:** Inspect or rewrite Terraform state depending on subcommand; potentially high-risk.

**Syntax:** `terraform` is the executable; `state` selects subcommand; trailing operands/flags choose target and behavior. No named options; inspect positional arguments.

**Expected output:** Inspect or rewrite Terraform state depending on subcommand; potentially high-risk. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🔴 Can mutate real cloud resources or state. Requires a reviewed plan and recovery strategy.

