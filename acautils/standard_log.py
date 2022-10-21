from pathlib import Path
import logging
from acautils.version_handler import get_version


def setup_logger(path: Path, name: str) -> logging.Logger:
    """
    General method for setting op a log object. Ensures that the different logs we use across tools are
    standardized
    ## Args
    * path: a path object designating the root in the hand-in. The scripts then puts the .log file in the _metadata folder from that root, creating it if none exists.
    * name: the name of the log file, e.g. 'digiarchlog'. The .log extension is automatically added
    """
    log: logging.Logger = logging.getLogger(name)
    log_root: Path = path / "_metadata"
    log_root.mkdir(exist_ok=True)
    file_handler: logging.FileHandler = logging.FileHandler(
        log_root / (name + ".log"), "a", encoding="utf-8"
    )
    log_fmt: logging.Formatter = logging.Formatter(
        fmt="%(asctime)s %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handler.setFormatter(log_fmt)
    log.addHandler(file_handler)
    log.setLevel(logging.INFO)
    log.info(get_version())
    return log
