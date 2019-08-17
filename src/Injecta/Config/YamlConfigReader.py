from pathlib import Path
from Injecta.Config.ConfigPathsResolver import ConfigPathsResolver
from Injecta.Config.ConfigLoaderAndMerger import ConfigLoaderAndMerger

class YamlConfigReader:

    def __init__(self):
        self.__configPathsResolver = ConfigPathsResolver()
        self.__configLoaderAndMerger = ConfigLoaderAndMerger()

    def read(self, configPath: str):
        configPaths = self.__configPathsResolver.resolve(Path(configPath), Path(configPath).parent)

        return self.__configLoaderAndMerger.loadAndMerge(configPaths)
