import sys

if __package__ is None and not hasattr(sys, "frozen"):
    import os.path
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, os.path.realpath(path))

import owo

if __name__ == "__main__":
    output=owo.main()
    if output == None:
      print("an error might have occured...",file=sys.stderr)
    else:
      from yaml import dump
      print(dump(output))