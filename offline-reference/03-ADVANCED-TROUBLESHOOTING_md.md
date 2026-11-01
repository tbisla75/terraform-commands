# OFFLINE TERRAFORM / IAC REFERENCE: 03-ADVANCED-TROUBLESHOOTING.md

Works locally without ChatGPT. Derived directly from [03-ADVANCED-TROUBLESHOOTING.md](../03-ADVANCED-TROUBLESHOOTING.md). Every available command includes syntax, state safety and intended output. Validate provider-specific options and release constraints before application.

## 1. terraform init -reconfigure

```bash
terraform init -reconfigure
```

**Purpose:** Initialize provider modules and backend; downloads dependencies and may configure backend.

**Syntax:** `terraform` is the executable; `init` selects subcommand; trailing operands/flags choose target and behavior. `-reconfigure` = a CLI option; verify with installed help

**Expected output:** Initialize provider modules and backend; downloads dependencies and may configure backend. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 2. terraform providers

```bash
terraform providers
```

**Purpose:** Inspect provider dependencies and lockfile constraints.

**Syntax:** `terraform` is the executable; `providers` selects subcommand; trailing operands/flags choose target and behavior. No named options; inspect positional arguments.

**Expected output:** Inspect provider dependencies and lockfile constraints. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 3. terraform workspace show

```bash
terraform workspace show
```

**Purpose:** Manage logical state selection and workspace metadata.

**Syntax:** `terraform` is the executable; `workspace` selects subcommand; trailing operands/flags choose target and behavior. No named options; inspect positional arguments.

**Expected output:** Manage logical state selection and workspace metadata. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 4. terraform plan -lock-timeout=10m

```bash
terraform plan -lock-timeout=10m
```

**Purpose:** Calculate infrastructure changes and store optional sensitive plan file.

**Syntax:** `terraform` is the executable; `plan` selects subcommand; trailing operands/flags choose target and behavior. `-lock-timeout=10m` = a CLI option; verify with installed help

**Expected output:** Calculate infrastructure changes and store optional sensitive plan file. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 5. terraform plan -refresh-only

```bash
terraform plan -refresh-only
```

**Purpose:** Calculate infrastructure changes and store optional sensitive plan file.

**Syntax:** `terraform` is the executable; `plan` selects subcommand; trailing operands/flags choose target and behavior. `-refresh-only` = a CLI option; verify with installed help

**Expected output:** Calculate infrastructure changes and store optional sensitive plan file. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 6. terraform state list

```bash
terraform state list
```

**Purpose:** Inspect or rewrite Terraform state depending on subcommand; potentially high-risk.

**Syntax:** `terraform` is the executable; `state` selects subcommand; trailing operands/flags choose target and behavior. No named options; inspect positional arguments.

**Expected output:** Inspect or rewrite Terraform state depending on subcommand; potentially high-risk. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 7. terraform plan -target='module.network'

```bash
terraform plan -target='module.network'
```

**Purpose:** Calculate infrastructure changes and store optional sensitive plan file.

**Syntax:** `terraform` is the executable; `plan` selects subcommand; trailing operands/flags choose target and behavior. `-target='module.network'` = a CLI option; verify with installed help

**Expected output:** Calculate infrastructure changes and store optional sensitive plan file. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 8. terraform plan -replace='aws_instance.example'

```bash
terraform plan -replace='aws_instance.example'
```

**Purpose:** Calculate infrastructure changes and store optional sensitive plan file.

**Syntax:** `terraform` is the executable; `plan` selects subcommand; trailing operands/flags choose target and behavior. `-replace='aws_instance.example'` = a CLI option; verify with installed help

**Expected output:** Calculate infrastructure changes and store optional sensitive plan file. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 9. terraform import 'aws_instance.example' 'i-EXAMPLE'

```bash
terraform import 'aws_instance.example' 'i-EXAMPLE'
```

**Purpose:** Associate pre-existing infrastructure with Terraform state.

**Syntax:** `terraform` is the executable; `import` selects subcommand; trailing operands/flags choose target and behavior. No named options; inspect positional arguments.

**Expected output:** Associate pre-existing infrastructure with Terraform state. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🔴 Can mutate real cloud resources or state. Requires a reviewed plan and recovery strategy.

## 10. terraform state show 'aws_instance.example'

```bash
terraform state show 'aws_instance.example'
```

**Purpose:** Inspect or rewrite Terraform state depending on subcommand; potentially high-risk.

**Syntax:** `terraform` is the executable; `state` selects subcommand; trailing operands/flags choose target and behavior. No named options; inspect positional arguments.

**Expected output:** Inspect or rewrite Terraform state depending on subcommand; potentially high-risk. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 11. terraform version

```bash
terraform version
```

**Purpose:** Terraform CLI operation; check version-specific docs.

**Syntax:** `terraform` is the executable; `version` selects subcommand; trailing operands/flags choose target and behavior. No named options; inspect positional arguments.

**Expected output:** Terraform CLI operation; check version-specific docs. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 12. terraform providers

```bash
terraform providers
```

**Purpose:** Inspect provider dependencies and lockfile constraints.

**Syntax:** `terraform` is the executable; `providers` selects subcommand; trailing operands/flags choose target and behavior. No named options; inspect positional arguments.

**Expected output:** Inspect provider dependencies and lockfile constraints. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 13. terraform validate

```bash
terraform validate
```

**Purpose:** Statically validate Terraform configuration/schema.

**Syntax:** `terraform` is the executable; `validate` selects subcommand; trailing operands/flags choose target and behavior. No named options; inspect positional arguments.

**Expected output:** Statically validate Terraform configuration/schema. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 14. terraform console

```bash
terraform console
```

**Purpose:** Interactive Terraform expression console.

**Syntax:** `terraform` is the executable; `console` selects subcommand; trailing operands/flags choose target and behavior. No named options; inspect positional arguments.

**Expected output:** Interactive Terraform expression console. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 15. terraform show -json tfplan

```bash
terraform show -json tfplan
```

**Purpose:** Display state or saved plan; may contain secrets.

**Syntax:** `terraform` is the executable; `show` selects subcommand; trailing operands/flags choose target and behavior. `-json` = a CLI option; verify with installed help

**Expected output:** Display state or saved plan; may contain secrets. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

