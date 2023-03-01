# -*- coding: utf-8 -*-

from . import config
from . import output
import logging
import sys

__author__ = "arris kathery"
__copyright__ = "copyright 2023 brendan berger"
__license__ = ""
__maintainer__ = "arris kathery"
__email__ = "whotookelburg@hotmail.com"
__version__ = "0.0.0-alpha0"


def main() -> dict:
    
    out=output.OutputObject()

    try:
      # do shit 
    except KeyboardInterrupt:
        return {'_kbi':True}

