# __init__.py

from importlib import resources
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

# Version of the py-o365-smtp package
__version__ = "0.0.1"

# Read constant values from config file
_cfg = tomllib.loads(resources.read_text("py-o365-smtp", "config.toml"))
URL = _cfg["graph"]["endpoint"]