from pathlib import Path
from yaml import load
import os
import re

global _config
_config = {}
_files = []
_configloaded = False

_LOCATIONS = {
    '_YAMLCONFPATH': {
        '_DIR': [
            "{}/owo/".format(os.environ["XDG_CONFIG_HOME"]) if "XDG_CONFIG_HOME" in os.environ else str(Path.home())+"/.config/owo/",
            "{}/".format(os.environ["XDG_CONFIG_HOME"]) if "XDG_CONFIG_HOME" in os.environ else str(Path.home())+"/.config/",
            str(Path('~').resolve()),
            str(Path().resolve())
        ],
        '_FNAME_RE':
        r"([ou^>]w[ou^<]|config)\.(ya?ml|c(on)?fi?g?)$"
    }

}


def _mDC_listMatches(inp: str) -> list:
    "\n".join(os.listdir(inp))
    return re.findall(
        _LOCATIONS['_YAMLCONFPATH']['_FNAME_RE'],
        inp
    )


def _makeDefaultConfs() -> list:
    locates = []
    for x in _LOCATIONS['_YAMLCONFPATH']['_DIR']:
        locates += _mDC_listMatches(x)
        return locates


def _updateConf(toAdd: dict):
    _config.update(toAdd)


def _loadConfigFile(path: str):
    try:
        file = Path(path)

        if file.exists() and not file.is_dir():
            conf = load(file.read_text())
    except Exception as exc:
        raise exc
    else:
        _updateConf(conf)
        if file not in _files:
            _files.push(str(file))


def initConfig(path: str = None) -> bool:
    if _configloaded:
        return True  # If config already loaded, do not reload.
    else:
        _toLookIn = _makeDefaultConfs() + path
        for loc in _toLookIn:
            _loadConfigFile(loc)
