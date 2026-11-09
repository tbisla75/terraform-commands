# Offline command / configuration reference: `templates/openshift-ipi/install-config.azure.yaml`

Generated from repository source by `tools/build_offline_reference.py`. **22 items**. This copy works offline. No commands were executed.

⚠️ **Version-aware reference, not a substitute for vendor docs.** Every individual command is preserved with purpose, flags, placeholders, expected output and risk. Ambiguous flags are marked as command-specific. Always verify flags against your installed CLI.

**Original file:** [`templates/openshift-ipi/install-config.azure.yaml`](../templates/openshift-ipi/install-config.azure.yaml)

### 1. Configuration field apiVersion

**Source line:** 2. **Language:** yaml. **Full syntax:** apiVersion = v1

**What it does:** API/schema version of the Kubernetes/OpenShift resource or installer config.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 2. Configuration field baseDomain

**Source line:** 3. **Language:** yaml. **Full syntax:** baseDomain = example.com

**What it does:** DNS zone for OpenShift cluster API and application names.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 3. Configuration field metadata

**Source line:** 4. **Language:** yaml. **Full syntax:** metadata = 

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 4. Configuration field name

**Source line:** 5. **Language:** yaml. **Full syntax:** name = ocp-prod

**What it does:** Resource/cluster/host identity in the enclosing object.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 5. Configuration field compute

**Source line:** 6. **Language:** yaml. **Full syntax:** compute = 

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 6. Configuration field name

**Source line:** 7. **Language:** yaml. **Full syntax:** name = worker

**What it does:** Resource/cluster/host identity in the enclosing object.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 7. Configuration field replicas

**Source line:** 8. **Language:** yaml. **Full syntax:** replicas = 3

**What it does:** Desired count of worker, master or application instances; assess quorum/headroom.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 8. Configuration field controlPlane

**Source line:** 9. **Language:** yaml. **Full syntax:** controlPlane = 

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 9. Configuration field name

**Source line:** 10. **Language:** yaml. **Full syntax:** name = master

**What it does:** Resource/cluster/host identity in the enclosing object.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 10. Configuration field replicas

**Source line:** 11. **Language:** yaml. **Full syntax:** replicas = 3

**What it does:** Desired count of worker, master or application instances; assess quorum/headroom.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 11. Configuration field platform

**Source line:** 12. **Language:** yaml. **Full syntax:** platform = 

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 12. Configuration field azure

**Source line:** 13. **Language:** yaml. **Full syntax:** azure = 

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 13. Configuration field region

**Source line:** 14. **Language:** yaml. **Full syntax:** region = westeurope

**What it does:** Cloud region, availability and quota boundary.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 14. Configuration field networking

**Source line:** 15. **Language:** yaml. **Full syntax:** networking = 

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 15. Configuration field networkType

**Source line:** 16. **Language:** yaml. **Full syntax:** networkType = OVNKubernetes

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 16. Configuration field clusterNetwork

**Source line:** 17. **Language:** yaml. **Full syntax:** clusterNetwork = 

**What it does:** Pod overlay IP addresses; avoid overlap.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 17. Configuration field cidr

**Source line:** 18. **Language:** yaml. **Full syntax:** cidr = 10.128.0.0/14

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 18. Configuration field hostPrefix

**Source line:** 19. **Language:** yaml. **Full syntax:** hostPrefix = 23

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 19. Configuration field serviceNetwork

**Source line:** 20. **Language:** yaml. **Full syntax:** serviceNetwork = 

**What it does:** Cluster Service IP pool; avoid overlap.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 20. Configuration field pullSecret

**Source line:** 22. **Language:** yaml. **Full syntax:** pullSecret = 'REPLACE_WITH_VALID_REDHAT_PULL_SECRET_JSON'

**What it does:** Sensitive Red Hat registry credential; NEVER commit a real value.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 21. Configuration field sshKey

**Source line:** 23. **Language:** yaml. **Full syntax:** sshKey = 'ssh-ed25519 REPLACE_WITH_PUBLIC_KEY'

**What it does:** Public operator SSH key; never provide a private key.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 22. Configuration field publish

**Source line:** 24. **Language:** yaml. **Full syntax:** publish = Internal

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

