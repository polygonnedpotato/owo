import sys

if __package__ is None and not hasattr(sys, "frozen"):
    import os.path
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, os.path.realpath(path))

import owo

if __name__ == "__main__":
    output=owo.main()
    del owo
    if output.__contains__('_err'):
       #from yaml import dump
       #print("exception! check stderr!!")
       #print(dump(output),file=sys.stderr)
       from json import dumps
       print(dumps(output))
       sys.exit(1)
    if output.__contains__('_kb'):
        print("interupted by keyboard")
        sys.exit()
    else:
        pass # output results
