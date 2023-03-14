# -*- coding: utf-8 -*-
# TODO: clean this up
# TODO: load datafiles. if not found, either fail or install files (maybe)?
from .output.owoOutputClass import owoOutputClass
from . import datafiles
import logging
import sys

__author__ = "arris kathery"
__copyright__ = "copyright 2023 brendan berger"
__license__ = ""
__maintainer__ = "arris kathery"
__email__ = "whotookelburg@hotmail.com"
__version__ = "0.0.0-alpha0"

DEBUG = True


def main() -> owoOutputClass:
  # PART 1: init
  try:
    out = owoOutputClass()
  except Exception as exc:
    import traceback
    traceback.print_exc(exc, file=sys.stderr)
    sys.exit(1)
  else:
    pass
  # PART 2: load config/data files
  try:
    
