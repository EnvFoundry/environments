# Contributing

Develop an environment in its own EnvFoundry repository. Use this repository for the catalogue, shared connection guidance and cross-environment examples.

## Improve an existing environment

Read its README and contributor instructions. Start from a concrete research operation, workload or failure. Keep domain behavior in the environment and host-specific behavior in its adapters. Preserve existing inputs, outputs and stored records, or document a versioned migration.

Use a topic branch and a pull request against the EnvFoundry repository. Describe the behavior that changes and the relevant checks. Retain contributor history, source references and existing licences. Keep public text focused on what someone can use or reproduce.

## Add an environment

A useful environment has a clear research purpose, an installable implementation, documented inputs and outputs, an executable example and an explicit licence. State the needed hardware, software, data and credentials at the installation step where they matter.

Keep its source and releases independent. Add one entry to `catalog.json`, using a stable ID and a commit that contains the documented capabilities. Describe interfaces that exist; new interface names are allowed. Link the connection guide and at least one runnable example. Update both README tables and run `python validate.py`.

An environment need not support every interface. A native library or CLI is a useful starting point. Add an MCP or product adapter when it helps a real consumer; reuse the underlying operations.

## Maintain the catalogue

Keep entries small enough to scan. Detailed tool schemas and domain references belong in the environment repository. `reviewed_revision` ties claims to source; update it when capability metadata changes. Preserve stable IDs when renaming a repository. Breaking catalogue-format changes require a new `schema_version` and migration guidance.

Use additive metadata for optional domain detail. Propose a shared field only when multiple environments or consumers need the same meaning. Keep dependencies and large data out of this catalogue repository.

中文：环境功能在对应仓库开发，目录和跨环境约定在本仓库维护。新增环境需具备明确用途、可安装实现、输入输出说明、可运行示例和许可证。保留作者与来源，使用分支和 PR；更新中英文入口，只描述已经实现的能力。
