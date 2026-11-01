# Offline command / configuration reference: `03-ADVANCED-TROUBLESHOOTING.md`

Generated from repository source by `tools/build_offline_reference.py`. **15 items**. This copy works offline. No commands were executed.

⚠️ **Version-aware reference, not a substitute for vendor docs.** Every individual command is preserved with purpose, flags, placeholders, expected output and risk. Ambiguous flags are marked as command-specific. Always verify flags against your installed CLI.

**Original file:** [`03-ADVANCED-TROUBLESHOOTING.md`](../03-ADVANCED-TROUBLESHOOTING.md)

### 1. `terraform init -reconfigure`

**Source line:** 10  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform init -reconfigure
```

**What it does:** Download/setup providers/modules and initialize backend; changes local working files.

**Syntax:** terraform init -reconfigure. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Option:** `-reconfigure` — Command-specific option or abbreviated argument; verify with installed CLI help and vendor reference.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Download/setup providers/modules and initialize backend; changes local working files. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 2. `terraform providers`

**Source line:** 11  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform providers
```

**What it does:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive.

**Syntax:** terraform providers. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 3. `terraform workspace show`

**Source line:** 12  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform workspace show
```

**What it does:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive.

**Syntax:** terraform workspace show. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 4. `terraform plan -lock-timeout=10m`

**Source line:** 13  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform plan -lock-timeout=10m
```

**What it does:** Compute proposed infrastructure change plan (typically does not mutate managed infrastructure).

**Syntax:** terraform plan -lock-timeout=10m. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Option:** `-lock-timeout=10m` — Command-specific option or abbreviated argument; verify with installed CLI help and vendor reference.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Compute proposed infrastructure change plan (typically does not mutate managed infrastructure). Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 5. `terraform plan -refresh-only`

**Source line:** 14  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

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

### 6. `terraform state list`

**Source line:** 15  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform state list
```

**What it does:** Read or manipulate Terraform state; some subcommands are dangerous.

**Syntax:** terraform state list. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Read or manipulate Terraform state; some subcommands are dangerous. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 7. `terraform plan -target='module.network'`

**Source line:** 35  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform plan -target='module.network'
```

**What it does:** Compute proposed infrastructure change plan (typically does not mutate managed infrastructure).

**Syntax:** terraform plan -target=module.network. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Option:** `-target=module.network` — Command-specific option or abbreviated argument; verify with installed CLI help and vendor reference.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Compute proposed infrastructure change plan (typically does not mutate managed infrastructure). Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 8. `terraform plan -replace='aws_instance.example'`

**Source line:** 36  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform plan -replace='aws_instance.example'
```

**What it does:** Compute proposed infrastructure change plan (typically does not mutate managed infrastructure).

**Syntax:** terraform plan -replace=aws_instance.example. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Option:** `-replace=aws_instance.example` — Command-specific option or abbreviated argument; verify with installed CLI help and vendor reference.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Compute proposed infrastructure change plan (typically does not mutate managed infrastructure). Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 9. `terraform import 'aws_instance.example' 'i-EXAMPLE'`

**Source line:** 37  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform import 'aws_instance.example' 'i-EXAMPLE'
```

**What it does:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive.

**Syntax:** terraform import aws_instance.example i-EXAMPLE. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 10. `terraform state show 'aws_instance.example'`

**Source line:** 38  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform state show 'aws_instance.example'
```

**What it does:** Read or manipulate Terraform state; some subcommands are dangerous.

**Syntax:** terraform state show aws_instance.example. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Read or manipulate Terraform state; some subcommands are dangerous. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 11. `terraform version`

**Source line:** 56  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform version
```

**What it does:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive.

**Syntax:** terraform version. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 12. `terraform providers`

**Source line:** 57  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform providers
```

**What it does:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive.

**Syntax:** terraform providers. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 13. `terraform validate`

**Source line:** 58  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform validate
```

**What it does:** Check Terraform configuration syntax and type/schema consistency.

**Syntax:** terraform validate. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Check Terraform configuration syntax and type/schema consistency. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 14. `terraform console`

**Source line:** 59  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform console
```

**What it does:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive.

**Syntax:** terraform console. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 15. `terraform show -json tfplan`

**Source line:** 60  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform show -json tfplan
```

**What it does:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive.

**Syntax:** terraform show -json tfplan. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Option:** `-json` — Command-specific option or abbreviated argument; verify with installed CLI help and vendor reference.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

