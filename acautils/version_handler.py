from pathlib import Path

def get_version() -> str:
    """
    Gets the version from the .toml file for the project it is currently loaded in to. If none can be found, returns unknown version
    """
    version: str = "Unknown version"
    with open(Path(__file__).absolute().parent.parent / "pyproject.toml") as i:
        for line in i.readlines():
            if line.startswith("version"):
                version = line[line.index('"') + 1 : -2]
    return version