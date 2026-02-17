import sys
from contextlib import chdir
from pathlib import Path
from subprocess import run, CalledProcessError

import pytest
from cookiecutter.main import cookiecutter

TEST_CONTENTS = {
    "project_name": "my-example-dashboard",
    "project_number": "R1972",
}


def test_smoke(tmp_path: Path):
    cookiecutter(
        template=".",
        output_dir=str(tmp_path),
        extra_context=TEST_CONTENTS,
        no_input=True,
    )


def test_function_prefix(tmp_path: Path):
    cookiecutter(
        template=".",
        output_dir=str(tmp_path),
        extra_context={
            "project_name": "nens-customer-dashboard",
            "project_number": "R1972",
        },
        no_input=True,
    )
    generated_dashboard_py = tmp_path / "nens-customer-dashboard/dashboard.py"
    # We prefix everything with our project name, but want to omit the '-dashboard'
    # part.
    print(generated_dashboard_py.read_text())  # For easier debugging
    assert 'page_title="nens-customer-dashboard"' in generated_dashboard_py.read_text()


def test_generated_project_ruff(tmp_path: Path):
    if sys.platform.startswith("win"):
        pytest.skip("Skipping test that uses linux commands")
    cookiecutter(
        template=".",
        output_dir=str(tmp_path),
        extra_context=TEST_CONTENTS,
        no_input=True,
    )
    with chdir(tmp_path / "my-example-dashboard"):
        run([sys.executable, "-m", "ruff", "format"], check=True)


def test_generated_project_precommit(tmp_path: Path):
    if sys.platform.startswith("win"):
        pytest.skip("Skipping test that uses linux commands")
    cookiecutter(
        template=".",
        output_dir=str(tmp_path),
        extra_context=TEST_CONTENTS,
        no_input=True,
    )
    with chdir(tmp_path / "my-example-dashboard"):
        run(["git", "init"], check=True)
        run(["git", "add", "-A"], check=True)
        try:
            run([sys.executable, "-m", "pre_commit", "run", "--all"], check=True)
        except CalledProcessError:
            print("pre-commit error, here is the 'git diff':")
            run(["git", "diff"])
            assert "format" == "ok"  # :-)


def test_generated_project_install(tmp_path: Path):
    if sys.platform.startswith("win"):
        pytest.skip("Skipping test that uses linux commands")
    cookiecutter(
        template=".",
        output_dir=str(tmp_path),
        extra_context=TEST_CONTENTS,
        no_input=True,
    )
    with chdir(tmp_path / "my-example-dashboard"):
        run(["uv", "sync"], check=True)
