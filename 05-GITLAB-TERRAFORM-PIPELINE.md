# Terraform delivery through GitLab CI/CD — review and controlled apply

Enterprise workflow: MR → format/validate → policy scan → plan artifact → peer review → protected-branch approved apply. Use remote encrypted locked state and short-lived workload identity/OIDC to AWS/Azure/GCP rather than static cloud keys.

### .gitlab-ci.yml starter

```yaml
stages: [validate, plan, deploy]
variables:
  TF_IN_AUTOMATION: "true"
  TF_INPUT: "false"
  TF_ROOT: "templates/cloud-managed/aws-eks"
  TF_CLI_CONFIG_FILE: "$CI_PROJECT_DIR/.terraformrc"

validate:
  stage: validate
  image: hashicorp/terraform:1.13
  script:
    - cd "$TF_ROOT"
    - terraform fmt -check -recursive
    - terraform init -backend=false
    - terraform validate
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
    - if: '$CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH'

plan:
  stage: plan
  image: hashicorp/terraform:1.13
  script:
    - cd "$TF_ROOT"
    - terraform init -lock-timeout=5m
    - terraform plan -lock-timeout=5m -out=tfplan
  artifacts:
    access: maintainer
    expire_in: 1 day
    paths:
      - "$TF_ROOT/tfplan"
  rules:
    - if: '$CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH'

apply:
  stage: deploy
  image: hashicorp/terraform:1.13
  needs:
    - job: plan
      artifacts: true
  script:
    - cd "$TF_ROOT"
    - terraform init -lock-timeout=5m
    - terraform apply -lock-timeout=5m tfplan
  resource_group: production-infrastructure
  environment:
    name: production
  when: manual
  rules:
    - if: '$CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH'
```

**Caution:** Pin the Terraform image to an approved digest before production. Artifact retention includes sensitive plan data: restrict access and use encrypted backend/artifacts. This is a starter; actual OIDC federation, provider authentication, scoped project runners, state backend and `checkov`/`trivy` policy gates must be configured before enabling apply. Confirm GitLab CI version supports artifact access semantics. Don't assume `terraform init -backend=false` can validate every provider without credentials.

### CLI review

```bash
terraform fmt -check -recursive
terraform init
terraform validate
terraform plan -lock-timeout=5m -out=tfplan
terraform show -no-color tfplan
terraform apply tfplan
```

<details><summary>🧠 Explain every pipeline CLI command in ChatGPT</summary>

- [1. Explain `terraform fmt -check -recursive`](https://chatgpt.com/?q=Explain%20Terraform%20CLI%20syntax%20of%20terraform%20fmt%20-check%20-recursive%20including%20every%20flag%2C%20state%20impacts%2C%20security%2C%20CI%20safeguards%20and%20recovery.)
- [2. Explain `terraform init`](https://chatgpt.com/?q=Explain%20Terraform%20CLI%20syntax%20of%20terraform%20init%20including%20every%20flag%2C%20state%20impacts%2C%20security%2C%20CI%20safeguards%20and%20recovery.)
- [3. Explain `terraform validate`](https://chatgpt.com/?q=Explain%20Terraform%20CLI%20syntax%20of%20terraform%20validate%20including%20every%20flag%2C%20state%20impacts%2C%20security%2C%20CI%20safeguards%20and%20recovery.)
- [4. Explain `terraform plan -lock-timeout=5m -out=tfplan`](https://chatgpt.com/?q=Explain%20Terraform%20CLI%20syntax%20of%20terraform%20plan%20-lock-timeout%3D5m%20-out%3Dtfplan%20including%20every%20flag%2C%20state%20impacts%2C%20security%2C%20CI%20safeguards%20and%20recovery.)
- [5. Explain `terraform show -no-color tfplan`](https://chatgpt.com/?q=Explain%20Terraform%20CLI%20syntax%20of%20terraform%20show%20-no-color%20tfplan%20including%20every%20flag%2C%20state%20impacts%2C%20security%2C%20CI%20safeguards%20and%20recovery.)
- [6. Explain `terraform apply tfplan`](https://chatgpt.com/?q=Explain%20Terraform%20CLI%20syntax%20of%20terraform%20apply%20tfplan%20including%20every%20flag%2C%20state%20impacts%2C%20security%2C%20CI%20safeguards%20and%20recovery.)

</details>

**Rollback warning:** Terraform is declarative reconciliation, not an instant undo. Reverting Git can destroy/replace resources. Recover from state backups and approved infrastructure plans, never blindly run `terraform destroy` or remove locks.

Sources: https://docs.gitlab.com/ci/ · https://developer.hashicorp.com/terraform/cli .
