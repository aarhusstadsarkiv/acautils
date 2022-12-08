# acautils
A shared repo, containing utility scripts for small, shared functionality between the different ACA tools

# Utilities
## Standard_log
A standard setup for a log object. Makes the format for loggers the same across tools, increasing readability. The standard logging module in python is very complex and very much to powerfull for our simple logging needs. The setup standard_log module is meant to provide a simple and reusable interface to ensure we can maintain a high quality of logging across tools.
### Usage
Say you have a system defined so:
```
root/
├─ module1/
│  ├─ sub_module2/
│  │  ├─ functionality1.py
│  │  ├─ functionality2.py
│  ├─ sub_module1/
│  ├─ main.py
├─ module2/
|  ├─ functionality3.py
```

In order to integrate the logger, in the `main.py` file you import the `setup_log` function and defines the log as a script-level object with (meaning at base indentation). In all other modules, you then use the function call `logging.getLogger("base_name_of_logger.module_name")` to setup a child of the defined logger in main. The log is then accessible by all scripts called from the module, even of the scripts are called from other scripts outside the module. 
E.g. let's say `main.py` called a function in `functionality1.py` and also in `functionality3.py`. Each of these scripts then log to their respective descendant logs, which is propagated up to the parent log, the base log, and then written to the file specified by that logs handler. 

## Version_handler
Gets and displays the version number in a uniform way for every tool. Requires a valid pyproject.toml file containing the version number
