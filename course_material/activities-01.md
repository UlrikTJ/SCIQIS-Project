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

3. Try out basic git workflows on the command line. 
    - Start by creating a new repository on Github (this can be private). It's a good idea to include the suggested Python .gitignore file.
    - Copy the repository address from the green "Code" button and do, in your terminal `git clone <pasted-address>`
    - Within this new local repository, write some dummy code and practice staging (`git add`), committing, and pushing to the remote (origin).
    - On Github web, change one of the files and commit. Back in your local repo (in terminal), pull this change.
    - Create (checkout) a branch, do some changes there, push to remote, and merge back into the main branch.

4. Now try doing the same actions in the version control interface of your editor of choice. If using Jupyter Lab, you need the jupyterlab-git extension.

5. Try to create conflicting edits in different branches or locally and remote. See what happens when you try to checkout or pull the conflicting branch/remote. How do you solve the conflict?

6. If you're done or all of this is too easy, try looking into some of the more esoteric functions of git, for example by looking [here](https://ndpsoftware.com/git-cheatsheet.html) (should be safe although there's a certificate problem).

7. Alternatively, learn about how to use [pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) or [issue tracking](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues) (which can also be used for keeping track of todos and bugs on personal projects). 