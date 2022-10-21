import os
from pathlib import Path


def get_version() -> str:
    """
    Finds the version described in the `pyproject.toml` file. \n
    The function looks at the `__file__` dunder's parent. If it can not find the .toml file there, it recursivly moves up one directory, to a maximum of 6 recursions. If the file is never found, it returns `unknown version`
    """

    def open_toml_and_get_version(file: Path) -> str:
        """
        Utility function for `get_version()` function. Opens toml file and reads the version number
        ## args
        - file: Path to the .toml file
        """
        with open(file=file) as i:
            for line in i.readlines():
                if line.startswith("version"):
                    version: str = line[line.index('"') + 1 : -2]
        return version

    def get_version_recursive(
        optional_path: Path | None = None, max_depth: int | None = None
    ) -> str:
        """
        recursive utility function for the `get_version()` function
        ## args
        * Optional_path: is only used by the function itself, as it calls itself recursively. Gives the path to the directory it should look for the .toml file in
        * max_depth: is only used by the function itself, as it calls itself recursively. Ensures that the script will only call itself 6 times max
        """

        # default case
        version: str = "Unknown version"

        if max_depth == 0:
            return version

        # checks whether a path was input, otherwise uses standard path
        path_to_directory_to_iterate_over: Path = (
            optional_path if optional_path else Path(__file__).parent
        )

        # makes a list of the paths
        directory_as_iterable_list: map[Path] = map(
            Path, os.listdir(path_to_directory_to_iterate_over)
        )
        for file in directory_as_iterable_list:
            if file.name == "pyproject.toml":
                version = open_toml_and_get_version(file)
                return version

        # if the .toml file isn't found, call the script again, this time on the parent
        if not max_depth:
            return get_version_recursive(
                path_to_directory_to_iterate_over.parent, 5
            )  # only do 5 more iterations
        else:
            return get_version_recursive(
                path_to_directory_to_iterate_over.parent, max_depth=max_depth - 1
            )

    return get_version_recursive()
