confDict = {}

def loadConfig(confLocation = "$HOME/.config/owo.yaml"):
    from os import path
    if not path.exists(confLocation):
        
