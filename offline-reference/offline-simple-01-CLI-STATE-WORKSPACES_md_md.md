# Offline command / configuration reference: `offline-simple/01-CLI-STATE-WORKSPACES_md.md`

Generated from repository source by `tools/build_offline_reference.py`. **23 items**. This copy works offline. No commands were executed.

⚠️ **Version-aware reference, not a substitute for vendor docs.** Every individual command is preserved with purpose, flags, placeholders, expected output and risk. Ambiguous flags are marked as command-specific. Always verify flags against your installed CLI.

**Original file:** [`offline-simple/01-CLI-STATE-WORKSPACES_md.md`](../offline-simple/01-CLI-STATE-WORKSPACES_md.md)

### 1. `terraform version`

**Source line:** 8  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform version
```

**What it does:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive.

**Syntax:** terraform version. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 2. `terraform fmt -check -recursive`

**Source line:** 26  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

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

### 3. `terraform init`

**Source line:** 44  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform init
```

**What it does:** Download/setup providers/modules and initialize backend; changes local working files.

**Syntax:** terraform init. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Download/setup providers/modules and initialize backend; changes local working files. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 4. `terraform validate`

**Source line:** 62  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform validate
```

**What it does:** Check Terraform configuration syntax and type/schema consistency.

**Syntax:** terraform validate. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Check Terraform configuration syntax and type/schema consistency. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 5. `terraform plan -out=tfplan`

**Source line:** 80  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform plan -out=tfplan
```

**What it does:** Compute proposed infrastructure change plan (typically does not mutate managed infrastructure).

**Syntax:** terraform plan -out=tfplan. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Option:** `-out=tfplan` — Command-specific option or abbreviated argument; verify with installed CLI help and vendor reference.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Compute proposed infrastructure change plan (typically does not mutate managed infrastructure). Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 6. `terraform show tfplan`

**Source line:** 98  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform show tfplan
```

**What it does:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive.

**Syntax:** terraform show tfplan. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 7. `terraform apply tfplan`

**Source line:** 116  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **CHANGE / POSSIBLY MUTATING**

**Exact command:**

```bash
terraform apply tfplan
```

**What it does:** Apply proposed changes to real infrastructure and Terraform state.

**Syntax:** terraform apply tfplan. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Safety/rollback:** Check subcommand and flags; requires change review and appropriate access.
**Expected result:** Apply proposed changes to real infrastructure and Terraform state. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 8. `terraform output`

**Source line:** 134  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform output
```

**What it does:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive.

**Syntax:** terraform output. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 9. `terraform state list`

**Source line:** 152  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform state list
```

**What it does:** Read or manipulate Terraform state; some subcommands are dangerous.

**Syntax:** terraform state list. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Read or manipulate Terraform state; some subcommands are dangerous. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 10. `terraform state show 'module.example.aws_instance.node'`

**Source line:** 170  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform state show 'module.example.aws_instance.node'
```

**What it does:** Read or manipulate Terraform state; some subcommands are dangerous.

**Syntax:** terraform state show module.example.aws_instance.node. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Read or manipulate Terraform state; some subcommands are dangerous. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 11. `terraform providers`

**Source line:** 188  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform providers
```

**What it does:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive.

**Syntax:** terraform providers. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 12. `terraform output -json`

**Source line:** 206  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform output -json
```

**What it does:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive.

**Syntax:** terraform output -json. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Option:** `-json` — Command-specific option or abbreviated argument; verify with installed CLI help and vendor reference.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 13. `terraform show -json tfplan`

**Source line:** 224  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

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

### 14. `terraform init -upgrade`

**Source line:** 242  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **CHANGE / POSSIBLY MUTATING**

**Exact command:**

```bash
terraform init -upgrade
```

**What it does:** Download/setup providers/modules and initialize backend; changes local working files.

**Syntax:** terraform init -upgrade. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Option:** `-upgrade` — Command-specific option or abbreviated argument; verify with installed CLI help and vendor reference.
**Safety/rollback:** Check subcommand and flags; requires change review and appropriate access.
**Expected result:** Download/setup providers/modules and initialize backend; changes local working files. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 15. `terraform providers lock -platform=linux_amd64 -platform=darwin_arm64`

**Source line:** 260  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform providers lock -platform=linux_amd64 -platform=darwin_arm64
```

**What it does:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive.

**Syntax:** terraform providers lock -platform=linux_amd64 -platform=darwin_arm64. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Option:** `-platform=linux_amd64` — Command-specific option or abbreviated argument; verify with installed CLI help and vendor reference.
**Option:** `-platform=darwin_arm64` — Command-specific option or abbreviated argument; verify with installed CLI help and vendor reference.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 16. `terraform get -update`

**Source line:** 278  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **CHANGE / POSSIBLY MUTATING**

**Exact command:**

```bash
terraform get -update
```

**What it does:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive.

**Syntax:** terraform get -update. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Option:** `-update` — Command-specific option or abbreviated argument; verify with installed CLI help and vendor reference.
**Safety/rollback:** Check subcommand and flags; requires change review and appropriate access.
**Expected result:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 17. `terraform plan -refresh-only`

**Source line:** 296  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

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

### 18. `terraform import 'aws_instance.example' 'i-EXAMPLE'`

**Source line:** 314  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform import 'aws_instance.example' 'i-EXAMPLE'
```

**What it does:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive.

**Syntax:** terraform import aws_instance.example i-EXAMPLE. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 19. `terraform workspace list`

**Source line:** 332  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform workspace list
```

**What it does:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive.

**Syntax:** terraform workspace list. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 20. `terraform workspace show`

**Source line:** 350  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform workspace show
```

**What it does:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive.

**Syntax:** terraform workspace show. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 21. `terraform state pull`

**Source line:** 368  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform state pull
```

**What it does:** Read or manipulate Terraform state; some subcommands are dangerous.

**Syntax:** terraform state pull. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Read or manipulate Terraform state; some subcommands are dangerous. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 22. `terraform state mv 'aws_instance.old' 'aws_instance.new'`

**Source line:** 386  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform state mv 'aws_instance.old' 'aws_instance.new'
```

**What it does:** Read or manipulate Terraform state; some subcommands are dangerous.

**Syntax:** terraform state mv aws_instance.old aws_instance.new. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Read or manipulate Terraform state; some subcommands are dangerous. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

### 23. `terraform state rm 'aws_instance.retired'`

**Source line:** 404  |  **Tool/purpose:** Terraform infrastructure as code  |  **Impact:** **DIAGNOSTIC / REVIEW**

**Exact command:**

```bash
terraform state rm 'aws_instance.retired'
```

**What it does:** Read or manipulate Terraform state; some subcommands are dangerous.

**Syntax:** terraform state rm aws_instance.retired. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output.
**Safety/rollback:** Typically query-oriented; may still cause network traffic, load or output sensitive information.
**Expected result:** Read or manipulate Terraform state; some subcommands are dangerous. Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.
**Offline verification:** On target host use `Terraform infrastructure as code` vendor manual or installed `--help`; [online vendor reference](https://developer.hashicorp.com/terraform/cli/commands).

