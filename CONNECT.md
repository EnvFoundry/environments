# Connect an environment

Choose an environment from [catalog.json](catalog.json), install it on the execution host, then use one of its documented interfaces. A Python process, a shell, an MCP client and a research OS can be different clients of the same implementation.

## Entry points

Run these commands inside each project's installed Python environment.

| Environment | Prepare a connection | Direct entry point |
| --- | --- | --- |
| SeedEnv | `seedenv connect mcp --group scientific-basics --output basics-agent`; choose other modules or Scientific Writing as needed | `seedenv`; Python, TypeScript and Rust host clients; generated MCP entry point |
| IOP | `iop init`, `iop start`, then `iop connect --name bench --local` | `iop mcp`; Python/TypeScript clients and the service HTTP API |
| Optics–Photonics | `optics-photonics connect agentic-research-os --output optics-plugin` for a Research OS package; consult the connection guide for other hosts | `optics-photonics mcp`; Python/TypeScript clients and CLI |
| Data Engineering | `ai-data connect --root . --output data-engineering.local.json` | `ai-data serve --help`; Python and CLI |
| Agent Gym | `agent-gym connect --output agent-gym.mcp.json` | `python -m agent_gym mcp`; Python and JSON stdin/stdout agent execution |

The generated configuration records a command and arguments for a specific interpreter. Import it into a compatible host, or map those fields to that host's MCP settings. Keep separate interpreters for the environments and use absolute paths for host-managed subprocesses.

IOP and Optics–Photonics also provide host-specific packages. Agent Gym can generate Research OS configuration with `agent-gym connect --host research-os --output agent-gym.plugin.json`. Follow each project's guide for the supported host formats and current installation instructions.

## Local computers, remote machines and web products

- **Local agent:** start the environment through its generated stdio configuration, or call its Python/CLI interface.
- **Remote scientific computer:** install the environment on the machine that has the instrument drivers, solver, data or accelerator. IOP has named SSH and HTTP connections; Optics–Photonics documents running its MCP process over SSH. Data Engineering and Gym currently execute locally on the host where their process runs.
- **Web product:** the product backend or an installed local connector owns the connection to that host. A browser page alone does not execute software on the user's PC. Reuse the environment's service or a host-managed remote process, and return job identifiers and result references to the web client.

Remote transport and environment behavior are separate. MCP supplies tool interaction; SSH connects machines; a solver SDK supplies domain operations. Supporting one does not establish support for the others.

## Exchange results

Preserve environment/version, task or run identity, inputs, output locations and completion state. Scientific arrays also need units, axes and conventions. Large arrays and datasets remain in files or object storage; tool responses return bounded views and references.

Use the existing Data Engineering–Gym [experience cycle](https://github.com/EnvFoundry/Data-Engineering/blob/main/examples/experience_cycle.py) for a working data/trajectory handoff. Other combinations should be implemented as explicit examples or adapters in the relevant environment. The catalogue does not impose a new execution protocol.
