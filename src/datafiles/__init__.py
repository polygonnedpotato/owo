_config={}
_files=[]

_locations={
    '_yamlmainconf':[
        # Check current dir
        './owo.yaml',
        './owo.yml',
        './owo.conf',
        './owo.cfg',
        './.owo.yaml',
        './.owo.yml',
        './.owo.conf',
        './.owo.cfg',

        # Check home dir
        '~/owo.yaml',
        '~/owo.yml',
        '~/owo.conf',
        '~/owo.cfg',
        '~/.owo.yaml',
        '~/.owo.yml',
        '~/.owo.conf',
        '~/.owo.cfg'
    ]
}

from sys import platform

_locations._yamlmainconf+={
    'linux':[
        '{env.HOME}/owo.yaml',
        '{env.HOME}/owo.yml',
        '{env.HOME}/owo.conf',
        '{env.HOME}/owo.cfg',
        '{env.HOME}/.owo.yaml',
        '{env.HOME}/.owo.yml',
        '{env.HOME}/.owo.conf',
        '{env.HOME}/.owo.cfg'
    ],
    'linux2':self.linux
}[platform]

def loadConfig(path: str) -> bool:
