from pathlib import Path
import logging


def setup_logger(log_path: Path) -> logging.Logger:
    """
    General method for setting op a log object. Ensures that the different logs we use across tools are
    standardized
    ## Args
    * path: the path directly to the log´as a `txt` file
    """
    log: logging.Logger = logging.getLogger(log_path.name)
    file_handler: logging.FileHandler = logging.FileHandler(
        log_path, "a", encoding="utf-8"
    )
    log_fmt: logging.Formatter = logging.Formatter(
        fmt="%(asctime)s %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handler.setFormatter(log_fmt)
    log.addHandler(file_handler)
    log.setLevel(logging.INFO)
    return log
