# Setting up for SCIQIS

## Software

First of all, you need a terminal. While most things we do can be done in a GUI, some things are easier in the terminal – and you need to know your way around that. If you're on macOS or Linux, you've already got a nice terminal. On Windows, you have PowerShell, but the commands you will find in this course and in most places online will often not work there. I don't have any recent experience with Windows, but I believe the best approach is to install [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install). An alternative is [Git Bash](https://gitforwindows.org).

You probably already have one or more favourite IDE(s) for coding. Feel free to keep using them. But otherwise, I recommend using [JupyterLab](https://jupyter.org) and [Visual Studio Code](https://code.visualstudio.com).

Other pieces of software that you need to set up for this course are [git](https://git-scm.com) and [uv](https://docs.astral.sh/uv/). Python is of course also necessary, but 1) you supposedly already have it installed, and 2) uv will take care of it anyway.

Finally, you should create an account on [Github](https://github.com) if you don't already have one, and on [Discord](https://discord.com). You can also download the desktop clients for Github and Discord, but there's no need.

### VS Code

Install through your package manager or by [downloading the installer](https://code.visualstudio.com). 

Once installed, there are a few extensions to install as well. Search for them in the Extensions left side panel:

* Python (which also installs a few other extensions)
* Jupyter (which also installs a few other extensions)
* Ruff
* Docs View
* H5Web

### uv

uv is a modern package and project manager for Python. Follow the [instructions](https://docs.astral.sh/uv/getting-started/installation/) to install it. 

There seems to be many ways to install on Windows – unfortunately, I don't know which to recommend. 

It's simpler on Linux/macOS: just do `curl -LsSf https://astral.sh/uv/install.sh | sh`.

### git

Git is the default version control system these days (well, since long ago). Chances are you've already got it installed. If not, find it [here](https://git-scm.com/downloads). 

After installation, you'll want to do [basic configuration of git](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup), at least setting up your name and email address to attach to commits:

```
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
```

### Github authentication

To clone the course repository, Git needs to [authenticate with GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github). The easiest option is probably SSH:

1. Generate an SSH key pair.
2. Add the public key to your GitHub account.
3. Clone repositories using the SSH URL that you find under the big green "<> Code" button on Github. 

If you prefer HTTPS instead, use a personal access token rather than your GitHub password, and optionally configure [Git Credential Manager](https://github.com/git-ecosystem/git-credential-manager) to save it securely.

## Say hi

Join the Discord server for the course using [this link](https://discord.gg/6KjNBXyYy), and say Hi in the #welcome channel. Here, you should also provide your Github username, as we will use this for the project.

Please [change your nickname](https://support.discord.com/hc/en-us/articles/219070107-Server-Nicknames) on the server to make you recognisable in class.

## Clone the sciqis course repository

Most of the course material (including this file) is made available on the course's Github repository at https://github.com/qpit/sciqis. It will be continually updated during the course, and the simplest way to make sure you always have the latest files is to clone the repo to your local machine,

```
$ git clone git@github.com:qpit/sciqis.git
```

(or `git clone https://github.com/qpit/sciqis.git` if you authenticated with HTTPS)

and keep it updated by pulling/syncing regularly:

```
$ git pull
```

You may wish to work directly in the provided .ipynb notebooks. However, if you do that directly in your cloned repository, you will encounter merge conflicts next time you attempt a pull. The easiest way to avoid that is to create a copy of the notebooks for editing, either in the same repository or in a separate folder. 

> [!TIP] 
> If you wish to keep your own edits under version control, you could instead fork the repository and keep it synced to the upstream repo (i.e. `github.com/qpit/sciqis`). See [here](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/configuring-a-remote-repository-for-a-fork) and [here](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork).


## Create virtual environment

It is a very good idea to keep separate environments for separate projects. Virtual environments keep projects isolated, minimal and reproducible.

In this course, we will use the [uv package manager](https://docs.astral.sh/uv/) instead of the more common (at least within science) [Conda](https://conda.org) package manager. Conda and the [conda-forge](https://conda-forge.org) community package repository is the standard tool in scientific computing, and you're welcome to keep using it – but you should also try out uv. For heavy scientific packages with many non-Python dependencies, conda may still be the way to go. For the packages we will use in this course, uv works like a charm.

> [!TIP]
> I believe the best way to install Conda is through [Miniforge](https://github.com/conda-forge/miniforge). Also, [Mamba](https://github.com/mamba-org/mamba) is a faster drop-in replacement for conda.

uv works with "projects": A project is a folder with a `pyproject.toml` file describing the project, including its dependencies, and a virtual environment in the hidden `.venv` folder.  Follow these steps in your terminal to initiate a new environment that you can use for your work in the first days of the course. Python, as well as most of the necessary packages will already be installed.

1. Copy `pyproject.toml` from the cloned `sciqis` repository to a new folder (or [download](https://github.com/qpit/sciqis/blob/2026/pyproject.toml) directly).
2. From within the folder, run `uv sync`. This will create a virtual environment and install all the packages.
3. Run `uv run python -m ipykernel install --user --name "sciqis" --display-name "Python (sciqis)"`. This will install a Jupyter kernel from this environment into your global Jupyter installation.
4. Test that you can open Jupyter Lab and create a new notebook running on the "Python (sciqis)" kernel: `uv run jupyter lab`

