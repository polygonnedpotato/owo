import logging

# outputDict={
#         'status': 1,
#         'input': {
#             'argsRaw': sys.argv,
#             'streamObjects': []
#         },
#         'output': [],
#         'errors': []
#     }


class OutputObject:

  def __init__(self, type: int):
    self.OOType = [
      'HeaderTable', 'BasicInfoTable', 'AdvancedInfoTable', 'DebugInfoTable'
    ][type]
    if type == 0:
      import sys
      self.input = {'argsRaw': sys.argv, 'streamObjects': []}
      del sys
