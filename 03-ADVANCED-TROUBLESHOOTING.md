# Terraform enterprise incident and recovery runbook

> Review all plans before any `apply`. Never commit Terraform state, tfvars containing credentials or provider secrets. ChatGPT explanation links are generated using generic commands only.

## Stuck plan, lock, drift

Never expose state encryption keys or tokens; inspect CI/remote backend status before touching state.

```bash
terraform init -reconfigure
terraform providers
terraform workspace show
terraform plan -lock-timeout=10m
terraform plan -refresh-only
terraform state list
```

<details>
<summary>🧠 Explain each command and full syntax</summary>

- [Explain 1: `terraform init -reconfigure`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20init%20-reconfigure)
- [Explain 2: `terraform providers`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20providers)
- [Explain 3: `terraform workspace show`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20workspace%20show)
- [Explain 4: `terraform plan -lock-timeout=10m`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20plan%20-lock-timeout%3D10m)
- [Explain 5: `terraform plan -refresh-only`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20plan%20-refresh-only)
- [Explain 6: `terraform state list`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20state%20list)

</details>

## Resource imports and replacements

HIGH-RISK operations need approved change, selected resource and state backup.

```bash
terraform plan -target='module.network'
terraform plan -replace='aws_instance.example'
terraform import 'aws_instance.example' 'i-EXAMPLE'
terraform state show 'aws_instance.example'
```

<details>
<summary>🧠 Explain each command and full syntax</summary>

- [Explain 1: `terraform plan -target='module.network'`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20plan%20-target%3D'module.network')
- [Explain 2: `terraform plan -replace='aws_instance.example'`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20plan%20-replace%3D'aws_instance.example')
- [Explain 3: `terraform import 'aws_instance.example' 'i-EXAMPLE'`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20import%20'aws_instance.example'%20'i-EXAMPLE')
- [Explain 4: `terraform state show 'aws_instance.example'`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20state%20show%20'aws_instance.example')

</details>

## Provider debugging

Verbose logs can expose secrets; capture locally and sanitize.

```bash
terraform version
terraform providers
terraform validate
terraform console
terraform show -json tfplan
```

<details>
<summary>🧠 Explain each command and full syntax</summary>

- [Explain 1: `terraform version`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20version)
- [Explain 2: `terraform providers`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20providers)
- [Explain 3: `terraform validate`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20validate)
- [Explain 4: `terraform console`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20console)
- [Explain 5: `terraform show -json tfplan`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20show%20-json%20tfplan)

</details>

