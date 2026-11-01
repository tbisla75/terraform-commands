# Enterprise IaC security and GitLab pipeline hygiene

> Review all plans before any `apply`. Never commit Terraform state, tfvars containing credentials or provider secrets. ChatGPT explanation links are generated using generic commands only.

## Preflight and change review

Plan output may reveal sensitive values in some metadata; use protected CI artifacts.

```bash
terraform fmt -check -recursive
terraform init -backend=false
terraform validate
terraform plan -lock-timeout=5m -out=tfplan
terraform show -no-color tfplan
```

<details>
<summary>🧠 Explain each command and full syntax</summary>

- [Explain 1: `terraform fmt -check -recursive`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20fmt%20-check%20-recursive)
- [Explain 2: `terraform init -backend=false`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20init%20-backend%3Dfalse)
- [Explain 3: `terraform validate`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20validate)
- [Explain 4: `terraform plan -lock-timeout=5m -out=tfplan`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20plan%20-lock-timeout%3D5m%20-out%3Dtfplan)
- [Explain 5: `terraform show -no-color tfplan`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20show%20-no-color%20tfplan)

</details>

## Security scanning and module audit

Commands require installed external tools; enforce policy gates before apply.

```bash
trivy config .
checkov -d .
tflint --init
tflint --recursive
terraform providers
terraform providers lock -platform=linux_amd64
```

<details>
<summary>🧠 Explain each command and full syntax</summary>

- [Explain 1: `trivy config .`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20trivy%20config%20.)
- [Explain 2: `checkov -d .`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20checkov%20-d%20.)
- [Explain 3: `tflint --init`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20tflint%20--init)
- [Explain 4: `tflint --recursive`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20tflint%20--recursive)
- [Explain 5: `terraform providers`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20providers)
- [Explain 6: `terraform providers lock -platform=linux_amd64`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20providers%20lock%20-platform%3Dlinux_amd64)

</details>

## Troubleshooting plan drift

Audit live changes before refresh-only apply. Never use '-lock=false' as a shortcut.

```bash
terraform plan -refresh-only
terraform state list
terraform providers
terraform validate
terraform graph
```

<details>
<summary>🧠 Explain each command and full syntax</summary>

- [Explain 1: `terraform plan -refresh-only`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20plan%20-refresh-only)
- [Explain 2: `terraform state list`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20state%20list)
- [Explain 3: `terraform providers`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20providers)
- [Explain 4: `terraform validate`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20validate)
- [Explain 5: `terraform graph`](https://chatgpt.com/?q=Explain%20Terraform%20command%20and%20CLI%20syntax%2C%20every%20flag%2C%20expression%20or%20shell%20operator%2C%20preconditions%2C%20state%20effects%2C%20security%20risks%2C%20output%2C%20safe%20production%20use%20and%20rollback.%20Command%3A%20terraform%20graph)

</details>

