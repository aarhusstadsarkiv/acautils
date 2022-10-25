from pathlib import Path


def get_version(toml_abs: Path) -> str:
    """
    Gets the version from the `pyproject.toml` file in the project.
    ## Args
    - toml_abs: The absolute path to the `pyproject.toml` file 
    """
    version: str = "Unknown version"
    with open(file=toml_abs) as i:
        for line in i.readlines():
            if line.startswith("version"):
                version: str = line[line.index('"') + 1 : -2]
    return version