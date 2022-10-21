import subprocess
import pytest  # type: ignore


@pytest.fixture()
def poetry_version() -> str:
    """
    Fixture for getting a string representation of the output of the 'poetry version --short' command (Note: not the 'poetry --version' command)
    """
    poetry_process: subprocess.CompletedProcess[bytes] = subprocess.run(
        ["poetry", "version", "--short"], stdout=subprocess.PIPE
    )
    return str(poetry_process.stdout)
