"""Test for command line interface."""

import contextlib
import io
import os
import subprocess
import sys

import pytest

from opus_ui import entrypoint


def test_cli_version() -> None:
    """Test if the command line interface is installed correctly."""
    name = "opus-ui"
    env = os.environ.get("VIRTUAL_ENV", "")
    if env:
        if os.name == "nt":
            exe = f"{env}\\\\Scripts\\\\{name}.cmd"
            if not os.path.exists(exe):  # noqa: PTH110
                exe = f"{env}\\\\Scripts\\\\{name}.exe"
        else:
            exe = f"{env}/bin/{name}"
    else:
        exe = name
    out = subprocess.check_output((exe, "--version"), text=True, shell=False)
    assert "version" in out
    out = subprocess.check_output(
        (
            sys.executable,
            "-m",
            "opus_ui",
            "--version",
        ),
        text=True,
        shell=False,
    )
    assert "version" in out
    stdout = io.StringIO()
    with contextlib.redirect_stdout(stdout), pytest.raises(SystemExit):
        entrypoint(("--version",))
    assert "version" in stdout.getvalue()


def test_import() -> None:
    """Test if module entrypoint has correct imports."""
    import opus_ui.__main__  # NoQA: F401


def test_hello(caplog: pytest.LogCaptureFixture) -> None:
    """Test command hello."""
    name = "A super secret name"
    entrypoint(("hello", "--name", name))
    assert name in caplog.text
