# EnvFoundry

**Open environments for autonomous research.**

[中文](README.zh-CN.md) · [Catalogue](catalog.json) · [Connection guide](CONNECT.md) · [Contribute](CONTRIBUTING.md)

EnvFoundry is a workshop for building, maintaining and extending research environments. An environment brings together the software, resources, operations and records needed to do a kind of research. People and agents use the same underlying implementation.

This repository is the entry point. Each environment keeps its own source, dependencies, runtime and releases.

## Environments

| Environment | Working capabilities | Interfaces |
| --- | --- | --- |
| [SeedEnv](https://github.com/EnvFoundry/SeedEnv) | Scientific Basics, Scientific Writing, templates and selectable domain software; prepare only what is needed and reuse existing installations. | Python, TypeScript, Rust, CLI, MCP |
| [IOP](https://github.com/EnvFoundry/IOP) | Instrument operations, persistent experiments, physical conditions, unit-bearing readings and correlated uncertainty. | Python, TypeScript, CLI, HTTP, MCP |
| [Optics–Photonics AI Lab](https://github.com/EnvFoundry/Optics-Photonics-AI-Lab) | Optical software and independent integrations, solver environments, scientific programs, resumable studies and result analysis. | Python, TypeScript, CLI, MCP |
| [Data Engineering](https://github.com/EnvFoundry/Data-Engineering) | Source releases, lineage and splits, budgeted mixtures, indexed shards and resumable readers. | Python, CLI, MCP |
| [Verifiable Agent Gym](https://github.com/EnvFoundry/Verifiable-Agent-Gym) | Task packages, batched environment interactions, independent evaluation and grouped rollout export. | Python, CLI, MCP, JSON process protocol |
| [AI Evaluation](https://github.com/EnvFoundry/AI-Evaluation) | Benchmark execution, grouped statistical comparisons, judge calibration and existing-run imports. | Python, CLI, MCP, JSON process protocol |
| [HSS](https://github.com/EnvFoundry/HSS) | Humanities and social sciences: selected research modules, study design, material and empirical analysis, and manuscript assembly. | Python, TypeScript, CLI, HTTP, MCP, JSON process protocol |

These projects serve Agentic Research OS, coding agents, other research systems and direct human use. A host chooses an implemented interface; a dedicated integration is optional. Compatibility with an interface does not imply that every host release or external solver has been tested.

## Start with one environment

Clone the project you need from EnvFoundry and follow its installation guide. Keep a separate Python environment for each project: scientific libraries and MCP dependencies have different version requirements.

| Project | Python | Install from its checkout | Connection guide |
| --- | --- | --- | --- |
| SeedEnv | 3.11+ | `python -m pip install -e .` | [Modules and host preparation](https://github.com/EnvFoundry/SeedEnv/blob/main/docs/integration.md) |
| IOP | 3.10+ | `python -m pip install -e ".[agent]"` | [Instruments and hosts](https://github.com/EnvFoundry/IOP/blob/main/iop/connect/README.md) |
| Optics–Photonics | 3.10+ | `python -m pip install -e .` | [Solvers and hosts](https://github.com/EnvFoundry/Optics-Photonics-AI-Lab/blob/main/docs/CONNECT.md) |
| Data Engineering | 3.11+ | `python -m pip install -e ".[mcp]"` | [Data interfaces](https://github.com/EnvFoundry/Data-Engineering/blob/main/docs/integrations.md) |
| Agent Gym | 3.11+ | `python -m pip install -e ".[mcp]"` | [Agent installation](https://github.com/EnvFoundry/Verifiable-Agent-Gym/blob/main/docs/install.md) |
| AI Evaluation | 3.11+ | `python -m pip install -e ".[mcp]"` | [Evaluation interfaces](https://github.com/EnvFoundry/AI-Evaluation/blob/main/docs/connect.md) |
| HSS | 3.11+ | `python -m pip install -e .` | [Research workbench and hosts](https://github.com/EnvFoundry/HSS/blob/main/docs/hosts.md) |

Install the execution environment where its resources live. Instrument drivers belong on the laboratory computer; commercial scientific SDKs belong on a machine with the software and its licence. A web application connects through a host integration or service. [Connection guide](CONNECT.md).

## Compose existing capabilities

Data Engineering and Agent Gym already share a working task-to-experience path. With their repositories checked out side by side and both core packages installed in an environment, run from `Data-Engineering`:

```sh
python examples/experience_cycle.py --gym-tasks ../Verifiable-Agent-Gym/examples/sql-workload/tasks.jsonl --output runs/experience-cycle
```

It prepares SQL task data, collects grouped attempts, imports trajectories, composes data shards and checks reader restart. The example uses scripted policies. Replace the policy and connect your learner to study learning outcomes.

AI Evaluation adds a [working Gym–Evaluation–Data integration](https://github.com/EnvFoundry/AI-Evaluation/blob/main/docs/gym-integration.md): execute matched task populations, import verifier outcomes, compare policies with grouped uncertainty, and retain the same trajectories in data releases.

IOP and Optics–Photonics expose measured results and recorded episodes through their own interfaces. Further combinations should name the transferred quantities, units, file formats and run identities, and include a working example in the relevant project.

## Discover programmatically

[`catalog.json`](catalog.json) lists stable environment IDs, repositories, reviewed source revisions, interfaces, prerequisites and examples. [`catalog.schema.json`](catalog.schema.json) defines its format. The catalogue contains descriptive metadata; reading it does not install or execute software.

Consumers can fetch the catalogue or vendor a pinned copy. Use a repository commit or release to reproduce an installation. `reviewed_revision` records the source used for the entry; it is not an automatically updated latest-version pointer.

```sh
python -m pip install "jsonschema>=4,<5"
python validate.py
```

## Development home

New development and pull requests belong in the EnvFoundry repositories. Download current packages from [IOP releases](https://github.com/EnvFoundry/IOP/releases) and [Optics–Photonics releases](https://github.com/EnvFoundry/Optics-Photonics-AI-Lab/releases). The original repositories under `Cherish0925` retain their history, discussions, earlier releases and existing links. Each repository builds its own release attachments; Git synchronization preserves source history.

Use one development home per change. An existing personal-repository branch can be brought into its EnvFoundry counterpart through a pull request, retaining its commits. Publishing new releases from EnvFoundry is independent of the original releases.

## Extend the workshop

New research environments belong in their own repositories. Add an entry here when someone can install the environment and run a meaningful example. Shared conventions describe discovery and connection; domain models, execution engines and dependencies stay with the environment that owns them.

See [CONTRIBUTING.md](CONTRIBUTING.md) for development and catalogue changes. This directory is MIT-licensed. Each environment and external tool retains its own licence.
