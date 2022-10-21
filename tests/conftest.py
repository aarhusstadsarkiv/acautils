import subprocess
import pytest  # type: ignore


@pytest.fixture()
def poetry_version() -> str:
    """
    Fixture for getting a string representation of the output of the 'poetry version' command (not the 'poetry --version' command)
    """
    poetry_process: subprocess.CompletedProcess[bytes] = subprocess.run(
        ["poetry", "version"], stdout=subprocess.PIPE
    )
    return str(poetry_process.stdout)
