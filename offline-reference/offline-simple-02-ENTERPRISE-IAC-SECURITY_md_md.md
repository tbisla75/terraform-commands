# Offline command / configuration reference: `offline-simple/02-ENTERPRISE-IAC-SECURITY_md.md`

Generated from repository source by `tools/build_offline_reference.py`. **16 items**. This copy works offline. No commands were executed.

⚠️ **Version-aware reference, not a substitute for vendor docs.** Every individual command is preserved with purpose, flags, placeholders, expected output and risk. Ambiguous flags are marked as command-specific. Always verify flags against your installed CLI.

**Original file:** [`offline-simple/02-ENTERPRISE-IAC-SECURITY_md.md`](../offline-simple/02-ENTERPRISE-IAC-SECURITY_md.md)

### 1. `terraform fmt -check -recursive`

**Source line:** 8  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

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

### 2. `terraform init -backend=false`

**Source line:** 26  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform init -backend=false
```

**What it does:** Download/setup providers/modules and initialize backend; changes local working files.

**Syntax:** terraform init -backend=false. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Option:** `-backend=false` — Command-specific option or abbreviated argument; verify with installed CLI help and vendor reference.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Download/setup providers/modules and initialize backend; changes local working files. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 3. `terraform validate`

**Source line:** 44  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform validate
```

**What it does:** Check Terraform configuration syntax and type/schema consistency.

**Syntax:** terraform validate. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Check Terraform configuration syntax and type/schema consistency. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 4. `terraform plan -lock-timeout=5m -out=tfplan`

**Source line:** 62  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

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

### 5. `terraform show -no-color tfplan`

**Source line:** 80  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

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

### 6. `trivy config .`

**Source line:** 98  |  **Tool/purpose:** trivy operation  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
trivy config .
```

**What it does:** Command semantics depend on installed implementation; inspect its man page and --help.

**Syntax:** trivy config .. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Command semantics depend on installed implementation; inspect its man page and --help. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `trivy operation` vendor manual or installed `--help`; [online vendor reference](https://man7.org/linux/man-pages/).

### 7. `checkov -d .`

**Source line:** 116  |  **Tool/purpose:** checkov operation  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
checkov -d .
```

**What it does:** Command semantics depend on installed implementation; inspect its man page and --help.

**Syntax:** checkov -d .. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Option:** `-d` — Disk/device or directory flag depending on command.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Command semantics depend on installed implementation; inspect its man page and --help. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `checkov operation` vendor manual or installed `--help`; [online vendor reference](https://man7.org/linux/man-pages/).

### 8. `tflint --init`

**Source line:** 134  |  **Tool/purpose:** tflint operation  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
tflint --init
```

**What it does:** Command semantics depend on installed implementation; inspect its man page and --help.

**Syntax:** tflint --init. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Option:** `--init` — Command-specific option or abbreviated argument; verify with installed CLI help and vendor reference.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Command semantics depend on installed implementation; inspect its man page and --help. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `tflint operation` vendor manual or installed `--help`; [online vendor reference](https://man7.org/linux/man-pages/).

### 9. `tflint --recursive`

**Source line:** 152  |  **Tool/purpose:** tflint operation  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
tflint --recursive
```

**What it does:** Command semantics depend on installed implementation; inspect its man page and --help.

**Syntax:** tflint --recursive. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Option:** `--recursive` — Traverse nested directories.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Command semantics depend on installed implementation; inspect its man page and --help. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `tflint operation` vendor manual or installed `--help`; [online vendor reference](https://man7.org/linux/man-pages/).

### 10. `terraform providers`

**Source line:** 170  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform providers
```

**What it does:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive.

**Syntax:** terraform providers. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 11. `terraform providers lock -platform=linux_amd64`

**Source line:** 188  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform providers lock -platform=linux_amd64
```

**What it does:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive.

**Syntax:** terraform providers lock -platform=linux_amd64. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Option:** `-platform=linux_amd64` — Command-specific option or abbreviated argument; verify with installed CLI help and vendor reference.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 12. `terraform plan -refresh-only`

**Source line:** 206  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform plan -refresh-only
```

**What it does:** Compute proposed infrastructure change plan (typically does not mutate managed infrastructure).

**Syntax:** terraform plan -refresh-only. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Option:** `-refresh-only` — Command-specific option or abbreviated argument; verify with installed CLI help and vendor reference.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Compute proposed infrastructure change plan (typically does not mutate managed infrastructure). Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 13. `terraform state list`

**Source line:** 224  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform state list
```

**What it does:** Read or manipulate Terraform state; some subcommands are dangerous.

**Syntax:** terraform state list. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Read or manipulate Terraform state; some subcommands are dangerous. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 14. `terraform providers`

**Source line:** 242  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform providers
```

**What it does:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive.

**Syntax:** terraform providers. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 15. `terraform validate`

**Source line:** 260  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform validate
```

**What it does:** Check Terraform configuration syntax and type/schema consistency.

**Syntax:** terraform validate. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Check Terraform configuration syntax and type/schema consistency. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 16. `terraform graph`

**Source line:** 278  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform graph
```

**What it does:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive.

**Syntax:** terraform graph. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

