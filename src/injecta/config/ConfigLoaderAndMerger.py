from pathlib import Path
from typing import List
from injecta.config.ConfigLoader import ConfigLoader
from injecta.config.ConfigMerger import ConfigMerger

class ConfigLoaderAndMerger:

    def __init__(self):
        self.__configLoader = ConfigLoader()
        self.__configMerger = ConfigMerger()

    def loadAndMerge(self, configPaths: List[Path]):
        yamlConfig = {}

        for configPath in configPaths:
            newYamlConfig = self.__configLoader.load(configPath)

            if 'imports' in newYamlConfig:
                del newYamlConfig['imports']

            yamlConfig = self.__configMerger.merge(yamlConfig, newYamlConfig)

        return yamlConfig
