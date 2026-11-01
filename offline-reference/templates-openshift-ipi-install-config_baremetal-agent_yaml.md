# OFFLINE OpenShift installer syntax: templates/openshift-ipi/install-config.baremetal-agent.yaml

Local, standalone explanation of [original template](../templates/openshift-ipi/install-config.baremetal-agent.yaml). **Never include real pullSecret or private keys in Git.** This YAML is a supported-installer *starter*, not a production-ready or validated cluster design. Check selected OpenShift installer release schema before running.

## 1. `apiVersion` = `v1`

**Source line:** 3. **Purpose:** Defines a field in the parent OpenShift Installer/AgentConfig API object; field validity is release- and platform-specific.

**Full syntax:** YAML key `apiVersion` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 2. `baseDomain` = `example.internal`

**Source line:** 4. **Purpose:** DNS domain under which OpenShift API and application names are created.

**Full syntax:** YAML key `baseDomain` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 3. `metadata`

**Source line:** 5. **Purpose:** Metadata naming block; cluster identity and labels.

**Full syntax:** YAML key `metadata` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 4. `name` = `ocp-prod`

**Source line:** 6. **Purpose:** Resource or host identifier within its enclosing block.

**Full syntax:** YAML key `name` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 5. `compute`

**Source line:** 7. **Purpose:** Worker node pool specification.

**Full syntax:** YAML key `compute` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 6. `name` = `worker`

**Source line:** 8. **Purpose:** Resource or host identifier within its enclosing block.

**Full syntax:** YAML key `name` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 7. `replicas` = `3`

**Source line:** 9. **Purpose:** Number of corresponding worker/master nodes.

**Full syntax:** YAML key `replicas` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 8. `controlPlane`

**Source line:** 10. **Purpose:** Master/control plane node sizing and replicas.

**Full syntax:** YAML key `controlPlane` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 9. `name` = `master`

**Source line:** 11. **Purpose:** Resource or host identifier within its enclosing block.

**Full syntax:** YAML key `name` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 10. `replicas` = `3`

**Source line:** 12. **Purpose:** Number of corresponding worker/master nodes.

**Full syntax:** YAML key `replicas` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 11. `networking`

**Source line:** 13. **Purpose:** Pod/service/machine CIDR and CNI settings.

**Full syntax:** YAML key `networking` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 12. `networkType` = `OVNKubernetes`

**Source line:** 14. **Purpose:** Network plugin used by OpenShift.

**Full syntax:** YAML key `networkType` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 13. `machineNetwork`

**Source line:** 15. **Purpose:** Routable machine address range; must match physical subnet.

**Full syntax:** YAML key `machineNetwork` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 14. `cidr` = `192.0.2.0/24 # documentation-only; replace with actual routable customer CIDR`

**Source line:** 16. **Purpose:** Defines a field in the parent OpenShift Installer/AgentConfig API object; field validity is release- and platform-specific.

**Full syntax:** YAML key `cidr` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 15. `clusterNetwork`

**Source line:** 17. **Purpose:** Overlay/Pod IP pool.

**Full syntax:** YAML key `clusterNetwork` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 16. `cidr` = `10.128.0.0/14`

**Source line:** 18. **Purpose:** Defines a field in the parent OpenShift Installer/AgentConfig API object; field validity is release- and platform-specific.

**Full syntax:** YAML key `cidr` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 17. `hostPrefix` = `23`

**Source line:** 19. **Purpose:** Defines a field in the parent OpenShift Installer/AgentConfig API object; field validity is release- and platform-specific.

**Full syntax:** YAML key `hostPrefix` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 18. `serviceNetwork`

**Source line:** 20. **Purpose:** Cluster Service VIP subnet.

**Full syntax:** YAML key `serviceNetwork` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 19. `platform`

**Source line:** 22. **Purpose:** Cloud or bare-metal infrastructure provider selection.

**Full syntax:** YAML key `platform` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 20. `baremetal`

**Source line:** 23. **Purpose:** Defines a field in the parent OpenShift Installer/AgentConfig API object; field validity is release- and platform-specific.

**Full syntax:** YAML key `baremetal` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 21. `apiVIPs`

**Source line:** 24. **Purpose:** OpenShift API virtual IPs; reachable and reserved.

**Full syntax:** YAML key `apiVIPs` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 22. `ingressVIPs`

**Source line:** 26. **Purpose:** Application ingress router virtual IPs.

**Full syntax:** YAML key `ingressVIPs` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 23. `pullSecret` = `'REPLACE_WITH_VALID_REDHAT_PULL_SECRET_JSON'`

**Source line:** 28. **Purpose:** Sensitive registry entitlement and authentication JSON; never publish real value.

**Full syntax:** YAML key `pullSecret` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 24. `sshKey` = `'ssh-ed25519 REPLACE_WITH_PUBLIC_KEY'`

**Source line:** 29. **Purpose:** Public operator SSH key, never a private key.

**Full syntax:** YAML key `sshKey` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

