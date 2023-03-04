from pathlib import Path
from sys import platform
from yaml import load, dump
import os
from re import search, IGNORECASE
import collections.abc

_config={}
_files=[]
_configloaded = False

_LOCATIONS = {
    '_YAMLCONFPATH':{
        '_DIR':[
            "{}/owo/".format(os.environ["XDG_CONFIG_HOME"]) if "XDG_CONFIG_HOME" in os.environ else str(Path.home())+"/.config/owo/",
            "{}/".format(os.environ["XDG_CONFIG_HOME"]) if "XDG_CONFIG_HOME" in os.environ else str(Path.home())+"/.config/",
            str(Path('~').resolve()),
            str(Path().resolve()) if str(Path.cwd()) not in self._DIRS else None
        ],
        '_FNAME_RE': 
            r"([ou^>]w[ou^<]|config)\.(ya?ml|c(on)?fi?g?)$"
    }

}

def _updateConf(toAdd: dict):
    for key, value in toAdd.items():
        if isinstance(value, collections.abc.Mapping):
            
def _loadYAMLConf(path: str):
    try:
        conf = yaml.load(file.read_text())
    except Exception as exc:
        # do an err
    else:
        if not _config:
            _config = conf
        else:
            


def initConfig(path: str) -> bool:
    if _configloaded:
        return True# If config already loaded, do not reload.
    else:
        try:
            file = Path(path)

            if file.exists() and not file.is_dir():
                try:
                    conf = yaml.load(file.read_text())
                except Exception as exc:
                    # do an err
                else:
                    if not _config
