# SCIQIS activities 01

## Environments

1. Think about your current Python environment. Discuss with your neighbour.
    - If you open a terminal and type `python` or `python3`, do you know where this executable lives?
    - Which packages are installed there?
    - Do you have any other environments (conda, virtualenv)? Do you know how to switch between them?
    - Do you use one environment for everything or per-project environments? Why?
    - How do you install new packages?

2. Try out the different functionalities of uv, following the tutorials listed in [references](./references.md). In particular
    - Initiate a new project with `uv init` and add packages with `uv add`. See what happens to `pyproject.toml` and what is listed by `uv pip list`.
    - From different folders within and outside the project, see what `which python` or `which python3` (possibly `where python`/`Get-Command python` on Windows) links to.
    - From within the project, check where Python is:\
      Try `uv run which python`\
      Try `uv run python -c 'import sys;print(sys.executable)'` and `uv run python -c 'import sys;print(sys._base_executable)`\
      Try `uv python list`
    - The continuous-variable quantum circuit simulator [Strawberry Fields](https://github.com/XanaduAI/strawberryfields) has not been updated to support newer version of Python, NumPy and SciPy. Try to set up an environment with uv that will make it run properly.

## Version control with git