# -*- coding: utf-8 -*-

# from . import config
from . import output
import logging
import sys

__author__ = "arris kathery"
__copyright__ = "copyright 2023 brendan berger"
__license__ = ""
__maintainer__ = "arris kathery"
__email__ = "whotookelburg@hotmail.com"
__version__ = "0.0.0-alpha0"

DEBUG = True

def main() -> dict:
    try:
        out=output.OutputObject()
    except Exception as exc:
        return {
            '_err':True,
            'exception':exc,
            'vars':{
                'globals': globals(),
                'locals': locals(),
                'dir': dir()
            }
        }
    try:
        pass
      # do shit 
    except KeyboardInterrupt:
        return {'_kbi':True}

