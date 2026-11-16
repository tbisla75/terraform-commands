# Offline command / configuration reference: `templates/openshift-ipi/agent-config.baremetal.yaml`

Generated from repository source by `tools/build_offline_reference.py`. **48 items**. This copy works offline. No commands were executed.

⚠️ **Version-aware reference, not a substitute for vendor docs.** Every individual command is preserved with purpose, flags, placeholders, expected output and risk. Ambiguous flags are marked as command-specific. Always verify flags against your installed CLI.

**Original file:** [`templates/openshift-ipi/agent-config.baremetal.yaml`](../templates/openshift-ipi/agent-config.baremetal.yaml)

### 1. Configuration field apiVersion

**Source line:** 3. **Language:** yaml. **Full syntax:** apiVersion = v1beta1

**What it does:** API/schema version of the Kubernetes/OpenShift resource or installer config.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 2. Configuration field kind

**Source line:** 4. **Language:** yaml. **Full syntax:** kind = AgentConfig

**What it does:** The resource type handled by the target API.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 3. Configuration field metadata

**Source line:** 5. **Language:** yaml. **Full syntax:** metadata = 

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 4. Configuration field name

**Source line:** 6. **Language:** yaml. **Full syntax:** name = ocp-prod

**What it does:** Resource/cluster/host identity in the enclosing object.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 5. Configuration field rendezvousIP

**Source line:** 7. **Language:** yaml. **Full syntax:** rendezvousIP = 192.0.2.21 # replace with reachable master-0 IP

**What it does:** Agent-based bootstrap rendezvous endpoint.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 6. Configuration field hosts

**Source line:** 8. **Language:** yaml. **Full syntax:** hosts = 

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 7. Configuration field hostname

**Source line:** 9. **Language:** yaml. **Full syntax:** hostname = master-0

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 8. Configuration field role

**Source line:** 10. **Language:** yaml. **Full syntax:** role = master

**What it does:** Selected node role or permissions context.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 9. Configuration field interfaces

**Source line:** 11. **Language:** yaml. **Full syntax:** interfaces = 

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 10. Configuration field name

**Source line:** 12. **Language:** yaml. **Full syntax:** name = eno1

**What it does:** Resource/cluster/host identity in the enclosing object.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 11. Configuration field macAddress

**Source line:** 13. **Language:** yaml. **Full syntax:** macAddress = "02:00:00:00:00:21"

**What it does:** Physical NIC hardware address; must match actual node.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 12. Configuration field rootDeviceHints

**Source line:** 14. **Language:** yaml. **Full syntax:** rootDeviceHints = 

**What it does:** Target boot disk selector; wrong values can wipe another drive.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 13. Configuration field deviceName

**Source line:** 15. **Language:** yaml. **Full syntax:** deviceName = /dev/sda

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 14. Configuration field hostname

**Source line:** 16. **Language:** yaml. **Full syntax:** hostname = master-1

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 15. Configuration field role

**Source line:** 17. **Language:** yaml. **Full syntax:** role = master

**What it does:** Selected node role or permissions context.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 16. Configuration field interfaces

**Source line:** 18. **Language:** yaml. **Full syntax:** interfaces = 

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 17. Configuration field name

**Source line:** 19. **Language:** yaml. **Full syntax:** name = eno1

**What it does:** Resource/cluster/host identity in the enclosing object.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 18. Configuration field macAddress

**Source line:** 20. **Language:** yaml. **Full syntax:** macAddress = "02:00:00:00:00:22"

**What it does:** Physical NIC hardware address; must match actual node.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 19. Configuration field rootDeviceHints

**Source line:** 21. **Language:** yaml. **Full syntax:** rootDeviceHints = 

**What it does:** Target boot disk selector; wrong values can wipe another drive.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 20. Configuration field deviceName

**Source line:** 22. **Language:** yaml. **Full syntax:** deviceName = /dev/sda

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 21. Configuration field hostname

**Source line:** 23. **Language:** yaml. **Full syntax:** hostname = master-2

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 22. Configuration field role

**Source line:** 24. **Language:** yaml. **Full syntax:** role = master

**What it does:** Selected node role or permissions context.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 23. Configuration field interfaces

**Source line:** 25. **Language:** yaml. **Full syntax:** interfaces = 

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 24. Configuration field name

**Source line:** 26. **Language:** yaml. **Full syntax:** name = eno1

**What it does:** Resource/cluster/host identity in the enclosing object.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 25. Configuration field macAddress

**Source line:** 27. **Language:** yaml. **Full syntax:** macAddress = "02:00:00:00:00:23"

**What it does:** Physical NIC hardware address; must match actual node.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 26. Configuration field rootDeviceHints

**Source line:** 28. **Language:** yaml. **Full syntax:** rootDeviceHints = 

**What it does:** Target boot disk selector; wrong values can wipe another drive.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 27. Configuration field deviceName

**Source line:** 29. **Language:** yaml. **Full syntax:** deviceName = /dev/sda

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 28. Configuration field hostname

**Source line:** 30. **Language:** yaml. **Full syntax:** hostname = worker-0

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 29. Configuration field role

**Source line:** 31. **Language:** yaml. **Full syntax:** role = worker

**What it does:** Selected node role or permissions context.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 30. Configuration field interfaces

**Source line:** 32. **Language:** yaml. **Full syntax:** interfaces = 

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 31. Configuration field name

**Source line:** 33. **Language:** yaml. **Full syntax:** name = eno1

**What it does:** Resource/cluster/host identity in the enclosing object.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 32. Configuration field macAddress

**Source line:** 34. **Language:** yaml. **Full syntax:** macAddress = "02:00:00:00:00:24"

**What it does:** Physical NIC hardware address; must match actual node.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 33. Configuration field rootDeviceHints

**Source line:** 35. **Language:** yaml. **Full syntax:** rootDeviceHints = 

**What it does:** Target boot disk selector; wrong values can wipe another drive.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 34. Configuration field deviceName

**Source line:** 36. **Language:** yaml. **Full syntax:** deviceName = /dev/sda

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 35. Configuration field hostname

**Source line:** 37. **Language:** yaml. **Full syntax:** hostname = worker-1

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 36. Configuration field role

**Source line:** 38. **Language:** yaml. **Full syntax:** role = worker

**What it does:** Selected node role or permissions context.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 37. Configuration field interfaces

**Source line:** 39. **Language:** yaml. **Full syntax:** interfaces = 

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 38. Configuration field name

**Source line:** 40. **Language:** yaml. **Full syntax:** name = eno1

**What it does:** Resource/cluster/host identity in the enclosing object.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 39. Configuration field macAddress

**Source line:** 41. **Language:** yaml. **Full syntax:** macAddress = "02:00:00:00:00:25"

**What it does:** Physical NIC hardware address; must match actual node.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 40. Configuration field rootDeviceHints

**Source line:** 42. **Language:** yaml. **Full syntax:** rootDeviceHints = 

**What it does:** Target boot disk selector; wrong values can wipe another drive.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 41. Configuration field deviceName

**Source line:** 43. **Language:** yaml. **Full syntax:** deviceName = /dev/sda

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 42. Configuration field hostname

**Source line:** 44. **Language:** yaml. **Full syntax:** hostname = worker-2

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 43. Configuration field role

**Source line:** 45. **Language:** yaml. **Full syntax:** role = worker

**What it does:** Selected node role or permissions context.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 44. Configuration field interfaces

**Source line:** 46. **Language:** yaml. **Full syntax:** interfaces = 

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 45. Configuration field name

**Source line:** 47. **Language:** yaml. **Full syntax:** name = eno1

**What it does:** Resource/cluster/host identity in the enclosing object.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 46. Configuration field macAddress

**Source line:** 48. **Language:** yaml. **Full syntax:** macAddress = "02:00:00:00:00:26"

**What it does:** Physical NIC hardware address; must match actual node.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 47. Configuration field rootDeviceHints

**Source line:** 49. **Language:** yaml. **Full syntax:** rootDeviceHints = 

**What it does:** Target boot disk selector; wrong values can wipe another drive.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 48. Configuration field deviceName

**Source line:** 50. **Language:** yaml. **Full syntax:** deviceName = /dev/sda

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

