from msilib.schema import Directory
import os
from pathlib import Path

def open_toml_and_get_version(file: Path) -> str:
    with open(file=file) as i:
        for line in i.readlines():
            if line.startswith("version"):
                version: str = line[line.index('"') + 1 : -2]
    return version


def get_version(optional_path: Path | None =None) -> str:
    """
    Gets the version from the .toml file for the project it is currently loaded in to. If none can be found, it recursively calls itself on the parent directory and looks for the toml file there. If no file is found and the script hits the users directory, return unknown version
    ## args
    * Optional_path: is only used by the function itself, as it calls itself recursively. Gives the path to the directory it should look for the .toml file in
    """

    version: str = "Unknown version"

    

    # checks whether a path was input, otherwise uses standard path
    path_to_directory_to_iterate_over: Path = optional_path if optional_path else Path(__file__).parent

    if path_to_directory_to_iterate_over.name == "Users": #HACK not the most graceful exit, but will do  
        # if we hit the users directory we are definitely to far in the file system. Return
        return version

    # makes a list of the paths
    directory_as_iterable_list: list[Path] = map(Path, os.listdir(path_to_directory_to_iterate_over))

    for file in directory_as_iterable_list:
        if file.name == "pyproject.toml":
            version = open_toml_and_get_version(file)
            return version
    
    # if the .toml file isn't found, call the script again, this time on the parent
    return get_version(path_to_directory_to_iterate_over.parent)
     
