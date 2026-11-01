# Terraform CLI: basic to advanced operations

> Review all plans before any `apply`. Never commit Terraform state, tfvars containing credentials or provider secrets. ChatGPT explanation links are generated using generic commands only.

## Basic workflow

Use a remote state backend with locking and scoped credentials.

```bash
terraform version
terraform fmt -check -recursive
terraform init
terraform validate
terraform plan -out=tfplan
terraform show tfplan
terraform apply tfplan
terraform output
```

<details>
<summary>🧠 Explain each command and full syntax</summary>

- [Explain 1: `terraform version`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20version)
- [Explain 2: `terraform fmt -check -recursive`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20fmt%20-check%20-recursive)
- [Explain 3: `terraform init`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20init)
- [Explain 4: `terraform validate`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20validate)
- [Explain 5: `terraform plan -out=tfplan`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20plan%20-out%3Dtfplan)
- [Explain 6: `terraform show tfplan`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20show%20tfplan)
- [Explain 7: `terraform apply tfplan`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20apply%20tfplan)
- [Explain 8: `terraform output`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20output)

</details>

## Inspect existing state

Sensitive state may include passwords, keys or internal addresses. Do not paste full state into ChatGPT.

```bash
terraform state list
terraform state show 'module.example.aws_instance.node'
terraform providers
terraform output -json
terraform show -json tfplan
```

<details>
<summary>🧠 Explain each command and full syntax</summary>

- [Explain 1: `terraform state list`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20state%20list)
- [Explain 2: `terraform state show 'module.example.aws_instance.node'`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20state%20show%20'module.example.aws_instance.node')
- [Explain 3: `terraform providers`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20providers)
- [Explain 4: `terraform output -json`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20output%20-json)
- [Explain 5: `terraform show -json tfplan`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20show%20-json%20tfplan)

</details>

## Modules, providers, import

Import requires a matching resource declaration, correct resource identity and permissions.

```bash
terraform init -upgrade
terraform providers lock -platform=linux_amd64 -platform=darwin_arm64
terraform get -update
terraform plan -refresh-only
terraform import 'aws_instance.example' 'i-EXAMPLE'
```

<details>
<summary>🧠 Explain each command and full syntax</summary>

- [Explain 1: `terraform init -upgrade`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20init%20-upgrade)
- [Explain 2: `terraform providers lock -platform=linux_amd64 -platform=darwin_arm64`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20providers%20lock%20-platform%3Dlinux_amd64%20-platform%3Ddarwin_arm64)
- [Explain 3: `terraform get -update`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20get%20-update)
- [Explain 4: `terraform plan -refresh-only`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20plan%20-refresh-only)
- [Explain 5: `terraform import 'aws_instance.example' 'i-EXAMPLE'`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20import%20'aws_instance.example'%20'i-EXAMPLE')

</details>

## Advanced state operations (HIGH RISK)

Only after state backup, peer review, change approval, correct workspace and remote lock ownership.

```bash
terraform workspace list
terraform workspace show
terraform state pull
terraform state mv 'aws_instance.old' 'aws_instance.new'
terraform state rm 'aws_instance.retired'
```

<details>
<summary>🧠 Explain each command and full syntax</summary>

- [Explain 1: `terraform workspace list`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20workspace%20list)
- [Explain 2: `terraform workspace show`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20workspace%20show)
- [Explain 3: `terraform state pull`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20state%20pull)
- [Explain 4: `terraform state mv 'aws_instance.old' 'aws_instance.new'`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20state%20mv%20'aws_instance.old'%20'aws_instance.new')
- [Explain 5: `terraform state rm 'aws_instance.retired'`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20state%20rm%20'aws_instance.retired')

</details>

