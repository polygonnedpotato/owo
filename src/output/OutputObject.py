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

    def __init__(self):
        self.status = 1
        import sys
        self.input = {
            'argsRaw': sys.argv,
            'streamObjects': []
        }
        del sys
        self.output = []
        self.errors = []
