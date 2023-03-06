from .NetworkPath                    import NetworkPath
from ...config.datafiles.owoDataFile import owoDataFile
from ...config                       import moduleConfig

class DownloadJob:

    def __init__(self,
                 url:    NetworkPath,
                 engine:       string = moduleConfig.source.network.engine,
                 engineConfig: dict = moduleConfig.source.network.engineConfig
