# EnvFoundry directory

This repository describes research environments. Runtime and domain changes belong in the corresponding environment repository.

- Read `catalog.json` first and follow the selected environment's own instructions.
- Keep entries tied to a source revision. Separate implemented interfaces, prerequisites and future integration work.
- Maintain the English and Chinese entry pages together. Prefer concise descriptions and working commands.
- Preserve stable IDs, existing consumers, licences and contributor history.
- Use a topic branch and pull request. Run `python validate.py` after catalogue or schema changes.
- Do not install every environment to inspect the directory. Each environment has its own dependencies and execution host.
