# OFFLINE TERRAFORM / IAC REFERENCE: 02-ENTERPRISE-IAC-SECURITY.md

Works locally without ChatGPT. Derived directly from [02-ENTERPRISE-IAC-SECURITY.md](../02-ENTERPRISE-IAC-SECURITY.md). Every available command includes syntax, state safety and intended output. Validate provider-specific options and release constraints before application.

## 1. terraform fmt -check -recursive

```bash
terraform fmt -check -recursive
```

**Purpose:** Reformat/validate configuration formatting.

**Syntax:** `terraform` is the executable; `fmt` selects subcommand; trailing operands/flags choose target and behavior. `-check` = a CLI option; verify with installed help; `-recursive` = a CLI option; verify with installed help

**Expected output:** Reformat/validate configuration formatting. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 2. terraform init -backend=false

```bash
terraform init -backend=false
```

**Purpose:** Initialize provider modules and backend; downloads dependencies and may configure backend.

**Syntax:** `terraform` is the executable; `init` selects subcommand; trailing operands/flags choose target and behavior. `-backend=false` = a CLI option; verify with installed help

**Expected output:** Initialize provider modules and backend; downloads dependencies and may configure backend. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 3. terraform validate

```bash
terraform validate
```

**Purpose:** Statically validate Terraform configuration/schema.

**Syntax:** `terraform` is the executable; `validate` selects subcommand; trailing operands/flags choose target and behavior. No named options; inspect positional arguments.

**Expected output:** Statically validate Terraform configuration/schema. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 4. terraform plan -lock-timeout=5m -out=tfplan

```bash
terraform plan -lock-timeout=5m -out=tfplan
```

**Purpose:** Calculate infrastructure changes and store optional sensitive plan file.

**Syntax:** `terraform` is the executable; `plan` selects subcommand; trailing operands/flags choose target and behavior. `-lock-timeout=5m` = a CLI option; verify with installed help; `-out=tfplan` = a CLI option; verify with installed help

**Expected output:** Calculate infrastructure changes and store optional sensitive plan file. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 5. terraform show -no-color tfplan

```bash
terraform show -no-color tfplan
```

**Purpose:** Display state or saved plan; may contain secrets.

**Syntax:** `terraform` is the executable; `show` selects subcommand; trailing operands/flags choose target and behavior. `-no-color` = a CLI option; verify with installed help

**Expected output:** Display state or saved plan; may contain secrets. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 6. trivy config .

```bash
trivy config .
```

**Purpose:** Shell/tool operation that prepares, inspects or automates infrastructure workflow.

**Syntax:** `trivy` is the executable; `config` selects subcommand; trailing operands/flags choose target and behavior. No named options; inspect positional arguments.

**Expected output:** Shell/tool operation that prepares, inspects or automates infrastructure workflow. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 7. checkov -d .

```bash
checkov -d .
```

**Purpose:** Shell/tool operation that prepares, inspects or automates infrastructure workflow.

**Syntax:** `checkov` is the executable; `-d` selects subcommand; trailing operands/flags choose target and behavior. `-d` = a CLI option; verify with installed help

**Expected output:** Shell/tool operation that prepares, inspects or automates infrastructure workflow. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 8. tflint --init

```bash
tflint --init
```

**Purpose:** Shell/tool operation that prepares, inspects or automates infrastructure workflow.

**Syntax:** `tflint` is the executable; `--init` selects subcommand; trailing operands/flags choose target and behavior. `--init` = a CLI option; verify with installed help

**Expected output:** Shell/tool operation that prepares, inspects or automates infrastructure workflow. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 9. tflint --recursive

```bash
tflint --recursive
```

**Purpose:** Shell/tool operation that prepares, inspects or automates infrastructure workflow.

**Syntax:** `tflint` is the executable; `--recursive` selects subcommand; trailing operands/flags choose target and behavior. `--recursive` = a CLI option; verify with installed help

**Expected output:** Shell/tool operation that prepares, inspects or automates infrastructure workflow. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 10. terraform providers

```bash
terraform providers
```

**Purpose:** Inspect provider dependencies and lockfile constraints.

**Syntax:** `terraform` is the executable; `providers` selects subcommand; trailing operands/flags choose target and behavior. No named options; inspect positional arguments.

**Expected output:** Inspect provider dependencies and lockfile constraints. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 11. terraform providers lock -platform=linux_amd64

```bash
terraform providers lock -platform=linux_amd64
```

**Purpose:** Inspect provider dependencies and lockfile constraints.

**Syntax:** `terraform` is the executable; `providers` selects subcommand; trailing operands/flags choose target and behavior. `-platform=linux_amd64` = a CLI option; verify with installed help

**Expected output:** Inspect provider dependencies and lockfile constraints. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 12. terraform plan -refresh-only

```bash
terraform plan -refresh-only
```

**Purpose:** Calculate infrastructure changes and store optional sensitive plan file.

**Syntax:** `terraform` is the executable; `plan` selects subcommand; trailing operands/flags choose target and behavior. `-refresh-only` = a CLI option; verify with installed help

**Expected output:** Calculate infrastructure changes and store optional sensitive plan file. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 13. terraform state list

```bash
terraform state list
```

**Purpose:** Inspect or rewrite Terraform state depending on subcommand; potentially high-risk.

**Syntax:** `terraform` is the executable; `state` selects subcommand; trailing operands/flags choose target and behavior. No named options; inspect positional arguments.

**Expected output:** Inspect or rewrite Terraform state depending on subcommand; potentially high-risk. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 14. terraform providers

```bash
terraform providers
```

**Purpose:** Inspect provider dependencies and lockfile constraints.

**Syntax:** `terraform` is the executable; `providers` selects subcommand; trailing operands/flags choose target and behavior. No named options; inspect positional arguments.

**Expected output:** Inspect provider dependencies and lockfile constraints. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 15. terraform validate

```bash
terraform validate
```

**Purpose:** Statically validate Terraform configuration/schema.

**Syntax:** `terraform` is the executable; `validate` selects subcommand; trailing operands/flags choose target and behavior. No named options; inspect positional arguments.

**Expected output:** Statically validate Terraform configuration/schema. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

## 16. terraform graph

```bash
terraform graph
```

**Purpose:** Render dependency graph.

**Syntax:** `terraform` is the executable; `graph` selects subcommand; trailing operands/flags choose target and behavior. No named options; inspect positional arguments.

**Expected output:** Render dependency graph. Compare with declared config and known backend state; do not expose plan output.

**Risk:** 🟢/🟠 Usually inspection or working-directory changes. State/outputs can include credentials.

