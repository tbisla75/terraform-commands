# OFFLINE OpenShift installer syntax: templates/openshift-ipi/install-config.azure.yaml

Local, standalone explanation of [original template](../templates/openshift-ipi/install-config.azure.yaml). **Never include real pullSecret or private keys in Git.** This YAML is a supported-installer *starter*, not a production-ready or validated cluster design. Check selected OpenShift installer release schema before running.

## 1. `apiVersion` = `v1`

**Source line:** 2. **Purpose:** Defines a field in the parent OpenShift Installer/AgentConfig API object; field validity is release- and platform-specific.

**Full syntax:** YAML key `apiVersion` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 2. `baseDomain` = `example.com`

**Source line:** 3. **Purpose:** DNS domain under which OpenShift API and application names are created.

**Full syntax:** YAML key `baseDomain` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 3. `metadata`

**Source line:** 4. **Purpose:** Metadata naming block; cluster identity and labels.

**Full syntax:** YAML key `metadata` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 4. `name` = `ocp-prod`

**Source line:** 5. **Purpose:** Resource or host identifier within its enclosing block.

**Full syntax:** YAML key `name` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 5. `compute`

**Source line:** 6. **Purpose:** Worker node pool specification.

**Full syntax:** YAML key `compute` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 6. `name` = `worker`

**Source line:** 7. **Purpose:** Resource or host identifier within its enclosing block.

**Full syntax:** YAML key `name` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 7. `replicas` = `3`

**Source line:** 8. **Purpose:** Number of corresponding worker/master nodes.

**Full syntax:** YAML key `replicas` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 8. `controlPlane`

**Source line:** 9. **Purpose:** Master/control plane node sizing and replicas.

**Full syntax:** YAML key `controlPlane` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 9. `name` = `master`

**Source line:** 10. **Purpose:** Resource or host identifier within its enclosing block.

**Full syntax:** YAML key `name` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 10. `replicas` = `3`

**Source line:** 11. **Purpose:** Number of corresponding worker/master nodes.

**Full syntax:** YAML key `replicas` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 11. `platform`

**Source line:** 12. **Purpose:** Cloud or bare-metal infrastructure provider selection.

**Full syntax:** YAML key `platform` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 12. `azure`

**Source line:** 13. **Purpose:** Defines a field in the parent OpenShift Installer/AgentConfig API object; field validity is release- and platform-specific.

**Full syntax:** YAML key `azure` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 13. `region` = `westeurope`

**Source line:** 14. **Purpose:** Cloud region; must be supported and have capacity/quota.

**Full syntax:** YAML key `region` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 14. `networking`

**Source line:** 15. **Purpose:** Pod/service/machine CIDR and CNI settings.

**Full syntax:** YAML key `networking` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 15. `networkType` = `OVNKubernetes`

**Source line:** 16. **Purpose:** Network plugin used by OpenShift.

**Full syntax:** YAML key `networkType` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 16. `clusterNetwork`

**Source line:** 17. **Purpose:** Overlay/Pod IP pool.

**Full syntax:** YAML key `clusterNetwork` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 17. `cidr` = `10.128.0.0/14`

**Source line:** 18. **Purpose:** Defines a field in the parent OpenShift Installer/AgentConfig API object; field validity is release- and platform-specific.

**Full syntax:** YAML key `cidr` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 18. `hostPrefix` = `23`

**Source line:** 19. **Purpose:** Defines a field in the parent OpenShift Installer/AgentConfig API object; field validity is release- and platform-specific.

**Full syntax:** YAML key `hostPrefix` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 19. `serviceNetwork`

**Source line:** 20. **Purpose:** Cluster Service VIP subnet.

**Full syntax:** YAML key `serviceNetwork` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 20. `pullSecret` = `'REPLACE_WITH_VALID_REDHAT_PULL_SECRET_JSON'`

**Source line:** 22. **Purpose:** Sensitive registry entitlement and authentication JSON; never publish real value.

**Full syntax:** YAML key `pullSecret` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 21. `sshKey` = `'ssh-ed25519 REPLACE_WITH_PUBLIC_KEY'`

**Source line:** 23. **Purpose:** Public operator SSH key, never a private key.

**Full syntax:** YAML key `sshKey` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

## 22. `publish` = `Internal`

**Source line:** 24. **Purpose:** Defines a field in the parent OpenShift Installer/AgentConfig API object; field validity is release- and platform-specific.

**Full syntax:** YAML key `publish` with scalar/list/map data; whitespace indentation, hyphen list markers and parent object determine interpretation. **Expected behavior:** only after installer consumes the config. **Safety:** protect cluster network, credentials, BMC/disk selections and avoid address overlap. Verify in matching installer docs.

