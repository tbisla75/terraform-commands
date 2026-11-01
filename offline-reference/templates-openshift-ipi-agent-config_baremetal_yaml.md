# OFFLINE OpenShift installer syntax: templates/openshift-ipi/agent-config.baremetal.yaml

Local, standalone explanation of [original template](../templates/openshift-ipi/agent-config.baremetal.yaml). **Never include real pullSecret or private keys in Git.** This YAML is a supported-installer *starter*, not a production-ready or validated cluster design. Check selected OpenShift installer release schema before running.

## 1. `apiVersion` = `v1beta1`

**Source line:** 3. **Purpose:** Defines a field in the parent OpenShift Installer/AgentConfig API object; field validity is release- and platform-specific.

**Full syntax:** YAML key `apiVersion` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 2. `kind` = `AgentConfig`

**Source line:** 4. **Purpose:** Defines a field in the parent OpenShift Installer/AgentConfig API object; field validity is release- and platform-specific.

**Full syntax:** YAML key `kind` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 3. `metadata`

**Source line:** 5. **Purpose:** Metadata naming block; cluster identity and labels.

**Full syntax:** YAML key `metadata` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 4. `name` = `ocp-prod`

**Source line:** 6. **Purpose:** Resource or host identifier within its enclosing block.

**Full syntax:** YAML key `name` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 5. `rendezvousIP` = `192.0.2.21 # replace with reachable master-0 IP`

**Source line:** 7. **Purpose:** Bootstrap agent discovery endpoint; must be one reachable control-plane host.

**Full syntax:** YAML key `rendezvousIP` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 6. `hosts`

**Source line:** 8. **Purpose:** Agent-config machine inventory with unique NIC and boot disk.

**Full syntax:** YAML key `hosts` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 7. `hostname` = `master-0`

**Source line:** 9. **Purpose:** Host machine DNS name and inventory identity.

**Full syntax:** YAML key `hostname` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 8. `role` = `master`

**Source line:** 10. **Purpose:** master or worker node function.

**Full syntax:** YAML key `role` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 9. `interfaces`

**Source line:** 11. **Purpose:** Physical NIC mapping by MAC and interface name.

**Full syntax:** YAML key `interfaces` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 10. `name` = `eno1`

**Source line:** 12. **Purpose:** Resource or host identifier within its enclosing block.

**Full syntax:** YAML key `name` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 11. `macAddress` = `"02:00:00:00:00:21"`

**Source line:** 13. **Purpose:** Exact discovered NIC MAC per physical host.

**Full syntax:** YAML key `macAddress` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 12. `rootDeviceHints`

**Source line:** 14. **Purpose:** Hints to select disk on which RHCOS is installed; **destructive** to target disk.

**Full syntax:** YAML key `rootDeviceHints` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 13. `deviceName` = `/dev/sda`

**Source line:** 15. **Purpose:** Disk identifier; verify to prevent overwriting wrong disk.

**Full syntax:** YAML key `deviceName` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 14. `hostname` = `master-1`

**Source line:** 16. **Purpose:** Host machine DNS name and inventory identity.

**Full syntax:** YAML key `hostname` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 15. `role` = `master`

**Source line:** 17. **Purpose:** master or worker node function.

**Full syntax:** YAML key `role` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 16. `interfaces`

**Source line:** 18. **Purpose:** Physical NIC mapping by MAC and interface name.

**Full syntax:** YAML key `interfaces` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 17. `name` = `eno1`

**Source line:** 19. **Purpose:** Resource or host identifier within its enclosing block.

**Full syntax:** YAML key `name` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 18. `macAddress` = `"02:00:00:00:00:22"`

**Source line:** 20. **Purpose:** Exact discovered NIC MAC per physical host.

**Full syntax:** YAML key `macAddress` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 19. `rootDeviceHints`

**Source line:** 21. **Purpose:** Hints to select disk on which RHCOS is installed; **destructive** to target disk.

**Full syntax:** YAML key `rootDeviceHints` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 20. `deviceName` = `/dev/sda`

**Source line:** 22. **Purpose:** Disk identifier; verify to prevent overwriting wrong disk.

**Full syntax:** YAML key `deviceName` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 21. `hostname` = `master-2`

**Source line:** 23. **Purpose:** Host machine DNS name and inventory identity.

**Full syntax:** YAML key `hostname` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 22. `role` = `master`

**Source line:** 24. **Purpose:** master or worker node function.

**Full syntax:** YAML key `role` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 23. `interfaces`

**Source line:** 25. **Purpose:** Physical NIC mapping by MAC and interface name.

**Full syntax:** YAML key `interfaces` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 24. `name` = `eno1`

**Source line:** 26. **Purpose:** Resource or host identifier within its enclosing block.

**Full syntax:** YAML key `name` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 25. `macAddress` = `"02:00:00:00:00:23"`

**Source line:** 27. **Purpose:** Exact discovered NIC MAC per physical host.

**Full syntax:** YAML key `macAddress` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 26. `rootDeviceHints`

**Source line:** 28. **Purpose:** Hints to select disk on which RHCOS is installed; **destructive** to target disk.

**Full syntax:** YAML key `rootDeviceHints` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 27. `deviceName` = `/dev/sda`

**Source line:** 29. **Purpose:** Disk identifier; verify to prevent overwriting wrong disk.

**Full syntax:** YAML key `deviceName` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 28. `hostname` = `worker-0`

**Source line:** 30. **Purpose:** Host machine DNS name and inventory identity.

**Full syntax:** YAML key `hostname` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 29. `role` = `worker`

**Source line:** 31. **Purpose:** master or worker node function.

**Full syntax:** YAML key `role` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 30. `interfaces`

**Source line:** 32. **Purpose:** Physical NIC mapping by MAC and interface name.

**Full syntax:** YAML key `interfaces` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 31. `name` = `eno1`

**Source line:** 33. **Purpose:** Resource or host identifier within its enclosing block.

**Full syntax:** YAML key `name` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 32. `macAddress` = `"02:00:00:00:00:24"`

**Source line:** 34. **Purpose:** Exact discovered NIC MAC per physical host.

**Full syntax:** YAML key `macAddress` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 33. `rootDeviceHints`

**Source line:** 35. **Purpose:** Hints to select disk on which RHCOS is installed; **destructive** to target disk.

**Full syntax:** YAML key `rootDeviceHints` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 34. `deviceName` = `/dev/sda`

**Source line:** 36. **Purpose:** Disk identifier; verify to prevent overwriting wrong disk.

**Full syntax:** YAML key `deviceName` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 35. `hostname` = `worker-1`

**Source line:** 37. **Purpose:** Host machine DNS name and inventory identity.

**Full syntax:** YAML key `hostname` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 36. `role` = `worker`

**Source line:** 38. **Purpose:** master or worker node function.

**Full syntax:** YAML key `role` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 37. `interfaces`

**Source line:** 39. **Purpose:** Physical NIC mapping by MAC and interface name.

**Full syntax:** YAML key `interfaces` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 38. `name` = `eno1`

**Source line:** 40. **Purpose:** Resource or host identifier within its enclosing block.

**Full syntax:** YAML key `name` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 39. `macAddress` = `"02:00:00:00:00:25"`

**Source line:** 41. **Purpose:** Exact discovered NIC MAC per physical host.

**Full syntax:** YAML key `macAddress` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 40. `rootDeviceHints`

**Source line:** 42. **Purpose:** Hints to select disk on which RHCOS is installed; **destructive** to target disk.

**Full syntax:** YAML key `rootDeviceHints` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 41. `deviceName` = `/dev/sda`

**Source line:** 43. **Purpose:** Disk identifier; verify to prevent overwriting wrong disk.

**Full syntax:** YAML key `deviceName` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 42. `hostname` = `worker-2`

**Source line:** 44. **Purpose:** Host machine DNS name and inventory identity.

**Full syntax:** YAML key `hostname` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 43. `role` = `worker`

**Source line:** 45. **Purpose:** master or worker node function.

**Full syntax:** YAML key `role` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 44. `interfaces`

**Source line:** 46. **Purpose:** Physical NIC mapping by MAC and interface name.

**Full syntax:** YAML key `interfaces` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 45. `name` = `eno1`

**Source line:** 47. **Purpose:** Resource or host identifier within its enclosing block.

**Full syntax:** YAML key `name` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 46. `macAddress` = `"02:00:00:00:00:26"`

**Source line:** 48. **Purpose:** Exact discovered NIC MAC per physical host.

**Full syntax:** YAML key `macAddress` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 47. `rootDeviceHints`

**Source line:** 49. **Purpose:** Hints to select disk on which RHCOS is installed; **destructive** to target disk.

**Full syntax:** YAML key `rootDeviceHints` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 48. `deviceName` = `/dev/sda`

**Source line:** 50. **Purpose:** Disk identifier; verify to prevent overwriting wrong disk.

**Full syntax:** YAML key `deviceName` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

