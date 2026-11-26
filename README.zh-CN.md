# EnvFoundry

**面向自主研究的开放环境。**

[English](README.md) · [环境目录](catalog.json) · [连接说明](CONNECT.md) · [参与开发](CONTRIBUTING.md)

EnvFoundry 是持续构建、维护和扩展研究环境的工坊。研究环境把一类工作所需的软件、资源、操作和记录组织起来，供研究人员与 Agent 使用。

这里提供统一入口。每个环境保留自己的代码、依赖、运行时和发布版本。

| 环境 | 已有能力 | 接口 |
| --- | --- | --- |
| [SeedEnv](https://github.com/EnvFoundry/SeedEnv) | 科研基础、科研写作、模板及各领域的软件模块；按需准备，复用已有安装。 | Python、TypeScript、Rust、CLI、MCP |
| [IOP](https://github.com/EnvFoundry/IOP) | 仪器操作、持久实验、物理工作条件、带单位读数和关联不确定度。 | Python、TypeScript、CLI、HTTP、MCP |
| [光学与光子学实验室](https://github.com/EnvFoundry/Optics-Photonics-AI-Lab) | 开源研究任务与软件、按任务关联的方法与程序、可接续的参数研究及可选外部接入。 | Python、TypeScript、CLI、MCP |
| [Data Engineering](https://github.com/EnvFoundry/Data-Engineering) | 数据版本、来源关系与划分、预算约束下的混合、索引分片和可恢复读取。 | Python、CLI、MCP |
| [Verifiable Agent Gym](https://github.com/EnvFoundry/Verifiable-Agent-Gym) | 任务包、批量环境交互、独立结果评价和分组轨迹导出。 | Python、CLI、MCP、JSON 进程协议 |
| [AI Evaluation](https://github.com/EnvFoundry/AI-Evaluation) | 基准执行、分组统计比较、评审校准和外部结果导入。 | Python、CLI、MCP、JSON 进程协议 |
| [HSS](https://github.com/EnvFoundry/HSS) | 人文社科：按需组合研究模块、形成研究方案、处理材料与实证分析、组织论文正文和结果表格。 | Python、TypeScript、CLI、HTTP、MCP、JSON 进程协议 |

这些环境面向 Agentic Research OS、coding agent、其他研究系统，也支持人直接使用。宿主选择已有接口即可接入；特定产品的插件是可选适配层。协议兼容与特定宿主、商业软件版本的实际测试分别记录。

## 安装与连接

从 EnvFoundry 克隆需要的仓库，按仓库说明安装。**每个环境使用独立的 Python 环境**，避免科学软件和 MCP 依赖的版本冲突。

| 环境 | Python | 在对应仓库内安装 | 连接说明 |
| --- | --- | --- | --- |
| SeedEnv | 3.11+ | `python -m pip install -e .` | [模块与宿主准备](https://github.com/EnvFoundry/SeedEnv/blob/main/docs/integration.md) |
| IOP | 3.10+ | `python -m pip install -e ".[agent]"` | [仪器与宿主](https://github.com/EnvFoundry/IOP/blob/main/iop/connect/README.md) |
| 光学与光子学 | 3.10+ | `python -m pip install -e .` | [求解器与宿主](https://github.com/EnvFoundry/Optics-Photonics-AI-Lab/blob/main/docs/CONNECT.md) |
| Data Engineering | 3.11+ | `python -m pip install -e ".[mcp]"` | [数据接口](https://github.com/EnvFoundry/Data-Engineering/blob/main/docs/integrations.md) |
| Agent Gym | 3.11+ | `python -m pip install -e ".[mcp]"` | [Agent 安装](https://github.com/EnvFoundry/Verifiable-Agent-Gym/blob/main/docs/install.md) |
| AI Evaluation | 3.11+ | `python -m pip install -e ".[mcp]"` | [评测接口](https://github.com/EnvFoundry/AI-Evaluation/blob/main/docs/connect.md) |
| HSS | 3.11+ | `python -m pip install -e .` | [研究工作台与宿主](https://github.com/EnvFoundry/HSS/blob/main/docs/hosts.md) |

执行环境部署在资源所在的计算机上：仪器驱动运行在实验电脑，商业求解器使用本机安装的软件、SDK 和许可证。Web 产品通过相应服务或本地连接组件调用环境。[连接说明](CONNECT.md) 列出具体入口。

## 已有的组合示例

Data Engineering 与 Agent Gym 已有贯通的数据流程。将两个仓库并列克隆，在同一 Python 环境中安装两个核心包，然后从 `Data-Engineering` 目录运行：

```sh
python examples/experience_cycle.py --gym-tasks ../Verifiable-Agent-Gym/examples/sql-workload/tasks.jsonl --output runs/experience-cycle
```

该示例完成 SQL 任务数据准备、分组尝试、轨迹导入、训练数据分片和读取恢复。示例使用脚本策略；学习效果需要接入实际模型和训练过程。

AI Evaluation 提供已贯通的 [Gym–Evaluation–Data 示例](https://github.com/EnvFoundry/AI-Evaluation/blob/main/docs/gym-integration.md)：执行相同任务总体，导入验证结果，进行分组统计比较，并把同一批轨迹保留在数据版本中。

IOP 与光学环境分别提供测量结果和实验轨迹。扩展组合时，在所属仓库提供可运行示例，并明确交换的物理量、单位、文件格式和运行标识。

## 供系统读取

[`catalog.json`](catalog.json) 保存稳定的环境 ID、仓库地址、查阅过的源代码版本、接口、运行条件和示例；[`catalog.schema.json`](catalog.schema.json) 定义格式。读取目录本身不会安装或执行软件。

系统可以获取目录，也可以固定一个版本随产品分发。复现实验时固定各环境的提交或发布版本。`reviewed_revision` 是目录描述对应的代码版本，并非自动追踪最新提交的指针。

## 后续开发

新开发和 PR 以 EnvFoundry 下的对应仓库为主。当前安装包可从 [IOP 发布页](https://github.com/EnvFoundry/IOP/releases)和[光学实验室发布页](https://github.com/EnvFoundry/Optics-Photonics-AI-Lab/releases)下载。`Cherish0925` 下的四个原仓库完整保留，已有提交、讨论、历史发布包和链接继续可用。各仓库分别构建发布附件；Git 同步保留源代码历史。

已有个人仓库分支可以通过 PR 纳入组织仓库，保留原提交。组织后续独立发布新版本，避免同一个改动在两个地方分别维护。

未来新环境独立建仓，提供明确的输入输出、安装入口和一个真实可运行的示例后，加入统一目录。共享约定保持简洁；领域模型、执行方式和依赖由各环境维护。

本目录使用 MIT 许可证，各研究环境及其调用的第三方工具保留各自许可证。[参与开发](CONTRIBUTING.md)。
