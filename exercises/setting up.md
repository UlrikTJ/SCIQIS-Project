# Setting up for SCIQIS

## Software

You probably already have one or more favourite IDE(s) for coding. Feel free to keep using them. But otherwise, I recommend using [JupyterLab](https://jupyter.org) and [Visual Studio Code](https://code.visualstudio.com).

Other pieces of software that you need to set up for this course are [git](https://git-scm.com) and [uv](https://docs.astral.sh/uv/). Python is of course also necessary, but 1) you supposedly already have it installed, and 2) uv will take care of it anyway.

Finally, you should create an account on [Github](https://github.com) if you don't already have one, and on [Discord](https://discord.com). You can also download the desktop clients for Github and Discord, but there's no need.

### VS Code

Install through your package manager or by [downloading the installer](https://code.visualstudio.com). 

Once installed, there are a few extensions to install as well. Search for them in the Extensions left side bar:

* Python (which also installs a few other extensions)
* Jupyter (which also installs a few other extensions)
* Github Copilot
* Docs View
* H5Web
* (Ruff?)

### uv

uv is a modern package and project manager for Python. Follow the [instructions](https://docs.astral.sh/uv/getting-started/installation/) to install it. 

There seems to be many ways to install on Windows – unfortunately, I don't know which to recommend. 

It's simpler on Linux/macOS: just do `curl -LsSf https://astral.sh/uv/install.sh | sh`.

### git

git is the default version control system these days. Chances are you've already got it installed. If not, find it [here](https://git-scm.com/downloads). 


## Say hi

Join the Discord server for the course using [this link](https://discord.gg/HVmxKyZg), and say Hi in the #welcome channel. Here, you should also provide your Github username, as we will use this for the project.

Feel free to [change your nickname](https://support.discord.com/hc/en-us/articles/219070107-Server-Nicknames) on the server to make you recognisable in class.

## Clone the sciqis course repository

Most of the course material (including this file) is made available on the course's Github repository at https://github.com/neago/sciqis. It will be continually updated during the course, and the simplest way to make sure you always have the latest files is to clone the repo to your local machine,

```
git clone git@github.com:neago/sciqis.git
```

and keep it updated by pulling/syncing regularly:

```
git pull
```

You may wish to work directly in the provided .ipynb notebooks. However, if you do that directly in your cloned repository, you will encounter merge conflicts next time you attempt a pull. The easiest way to avoid that is to create a copy of the notebooks for editing, either in the same repository or in a separate folder. 

> [!TIP] 
> If you wish to keep your own edits under version control, you could instead fork the repository and keep it synced to the upstream repo (i.e. `github.com/neago/sciqis`). See [here](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/configuring-a-remote-repository-for-a-fork) and [here](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork).