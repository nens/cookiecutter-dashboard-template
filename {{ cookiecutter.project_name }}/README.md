# {{ cookiecutter.project_name }} dashboard

## Post-generation checklist

First a little bit of github administration:

- Just making sure: you created a github repo and did the init/add/push shown after generating the project?
- Go to the ["manage access" page](https://github.com/nens/{{ cookiecutter.project_name }}/settings/access) and click "add teams": add the "adviseurs" team with **write** access. Otherwise you're the only one who can work on it.
- On that same page, add the team "nelen-schuurmans-pull-only" with **read** access. Otherwise the server cannot download the docker image.

If you're working on other dashboards, you *probably* have these two installed already:

- Install `uv`, it handles the virtualenv, the pip install, pinning versions. It also works much faster. [Here are the instructions](https://docs.astral.sh/uv/getting-started/installation/).
  - Afterwards: run `uv sync` to set up the project.
- To keep the code readable and maintainable, we use pre-commit. Install it with `pip install pre-commit` or `uv tool install pre-commit`.
  - Set up pre-commit to automatically run before every commit: `pre-commit install` (or just regulary run `pre-commit run --all`, that's also fine).

Lastly a bit of readme cleanup:

- In the next section, quickly add an initial sentence about the project.
- Remove this whole post-generation checklist from the readme. You won't need it anymore as you've diligently checked off every item :-)


## Project documentation

Project number: {{ cookiecutter.project_number }}.

TODO: add the documentation of your code here, what the aim is, etc.


## Development instructions

Some `uv` commands:

    $ uv sync  # Sets up the .venv and does the "pip install"
    $ uv add your-dependency  # If you need numpy or so; replaces requirements.txt
    $ uv run streamlit run dashboard.py
    $ uv sync --upgrade  # Allow upgrades to versions.


## Handy vscode setup: all ready for use

- If you use vscode and did the `uv sync` thingy above, the python plugin will detect your code and streamlit. So you'll have proper code completion! And type hints become more useful. (**Note**: you should have called `uv sync` first, before starting vscode, otherwise you have to select the python version manually: `.venv/bin/python` or so).
- Vscode will **recommend** "python", "editorconfig" and "ruff" extensions: install them. Vscode will ask about trusting "editorconfig" and "astral software": yes, that's okay.
  - Editorconfig handles unneeded spaces at the end of lines and other minutia.
  - Ruff formats your code and sorts the imports whenever you save a file. It will also warn about unknown variables or unused imports and offer fixes.
- The "run and debug" button has a "run dashboard with debugger" configuration. Run it and it will automatically start your dashboard in the browser. And you can set breakpoints and so in your code.

Nice, easy, modern development with mostly-automatic formatting and neatness!


## Deploying your dashboard to production

On every commit to the `main` branch, a new docker image is generated on github *if pre-commit doesn't complain* and *if the docker image can be build*. The server looks for new images every five minutes and downloads+restarts it automatically.

Should the github action complain about pre-commit, upgrade the config and run it again:

    $ pre-commit autoupdate
    $ pre-commit run --all

Should the github action fail on the docker image creation, try that one out locally and fix any errors:

    $ docker build .

Ask Reinout to add your new dashboard to the [dash-dashboards repo](https://github.com/nens/dash-dashboards).
