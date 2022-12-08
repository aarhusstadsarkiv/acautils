from pathlib import Path
import logging


def setup_logger(log_name: str, log_path: Path) -> logging.Logger:
    """
    General method for setting op a log object. Ensures that the different logs we use across tools are
    standardized
    ## Args
    * log_path: the path directly to the log as a `txt` file. If the file is not there, it will be created. If it already exists, it will append the messages to the file.
    * log_name: the name given to the logger within the logging modules own namespace. All descendant logs needs to have a name on the form 'log_name.descendant_log_name', which often is the name of the module or submodule that the function is called from.
    """
    # If the parents of the file does not exist, then we make them
    if not log_path.parent.exists():
        Path.mkdir(log_path.parent, parents=True, exist_ok=True)

    log: logging.Logger = logging.getLogger(log_name)
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
