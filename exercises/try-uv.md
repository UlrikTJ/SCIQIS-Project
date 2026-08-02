# Try uv

_Practice_

uv is an excellent package and project manager that you are highly recommended to use for all your work in SCIQIS.

Try out some of the basic functionalities of uv, following the tutorials listed below. In particular
    
- Initiate a new project with `uv init` and add packages with `uv add`. See what happens to `pyproject.toml` and what is listed by `uv pip list`.
- From different folders within and outside the project, see what `which python` or `which python3` (possibly `where python`/`Get-Command python` on Windows) links to.
- From within the project, check where Python is:
    - Try `uv run which python`
    - Try `uv run python -c 'import sys;print(sys.executable)'` and `uv run python -c 'import sys;print(sys._base_executable)`
    - Try `uv python list`
- The continuous-variable quantum circuit simulator [Strawberry Fields](https://github.com/XanaduAI/strawberryfields) has not been updated to support newer version of Python, NumPy and SciPy. Try to set up an environment with uv that will make it run properly.

Feel free to ask GenAI for assistance, but try to remember the basic commands.

## References

Docs: [uv official documentation](https://docs.astral.sh/uv/)

Tutorial: [Managing Python Projects With uv: An All-in-One Solution](https://realpython.com/python-uv/)

Tutorial: [Getting Started With uv, the Python Package & Project Manager](https://osc.garden/notes/uv/) - note that a few commands may be outdated

Reference: [uv cheatsheet](https://gist.github.com/gwangjinkim/70b353e63492e2bdd37f24b441b128b4)
