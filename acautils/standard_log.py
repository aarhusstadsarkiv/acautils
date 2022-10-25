from pathlib import Path
import logging
from acautils.version_handler import get_version


def setup_logger(path: Path, name: str) -> logging.Logger:
    """
    General method for setting op a log object. Ensures that the different logs we use across tools are
    standardized
    ## Args
    * path: a path object designating a directory where to put the `.log` file
    * name: the name of the log file, e.g. 'digiarchlog'. The `.log` extension is automatically added
    """
    log: logging.Logger = logging.getLogger(name)
    file_handler: logging.FileHandler = logging.FileHandler(
        path / (name + ".log"), "a", encoding="utf-8"
    )
    log_fmt: logging.Formatter = logging.Formatter(
        fmt="%(asctime)s %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handler.setFormatter(log_fmt)
    log.addHandler(file_handler)
    log.setLevel(logging.INFO)
    return log