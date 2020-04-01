from pathlib import Path
from typing import Dict, List
from injecta.config.ConfigPathsResolver import ConfigPathsResolver
from injecta.config.ConfigLoaderAndMerger import ConfigLoaderAndMerger
from injecta.config.ConfigReaderInterface import ConfigReaderInterface

class YamlConfigReader(ConfigReaderInterface):

    def __init__(self):
        self.__configPathsResolver = ConfigPathsResolver()
        self.__configLoaderAndMerger = ConfigLoaderAndMerger()

    def read(self, configPath: str):
        resolvedPaths = self.__configPathsResolver.resolve(Path(configPath), Path(configPath).parent)
        resolvedPathsByLevels = self.__toListByLevels(resolvedPaths)
        resolvedPathsByLevels.reverse()
        flattenedPaths = [item for sublist in resolvedPathsByLevels for item in sublist]

        return self.__configLoaderAndMerger.loadAndMerge(flattenedPaths)

    def __toListByLevels(self, resolvedPaths: List[Dict]):
        configPathsByLevels = dict()

        for resolvedPath in resolvedPaths:
            if resolvedPath['level'] not in configPathsByLevels:
                configPathsByLevels[resolvedPath['level']] = []

            configPathsByLevels[resolvedPath['level']].append(resolvedPath['path'])

        return list(configPathsByLevels.values())
