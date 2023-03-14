# TODO: clean this up
# TODO: complete dateFormat()
# TODO: complete stringFormat()

_DEFAULT = {
    '_DATETEMP':'%a, %d %b %Y %H:%M:%S %Z%z',
    '_INCLUDE':[
        'env',
    ]
}

def dateFormat(input: str = _DEFAULT._DATETEMP,use_local:bool=True) -> str:
    from time import strftime
    if use_local:
        from time import localtime
        return strftime(input,localtime())
    else:
        from time import gmtime
        return strftime(input,gmtime())

def stringFormat(
        input: str,
        include: list = _DEFAULT._INCLUDE
    ) -> str:

    imap = {
        'time': dateFormat()
    }

    if 'env' in include:
        import os
        imap['env'] = os.environ
        del os
    
    return input.format_map(imap)
