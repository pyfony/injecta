from typing import List, Dict
from injecta.config.ConfigLoader import ConfigLoader
from injecta.config.ImportDefinitionResolver import ImportDefinitionResolver
from pathlib import Path

class ConfigPathsResolver:

    def __init__(self):
        self.__configLoader = ConfigLoader()
        self.__importDefinitionResolver = ImportDefinitionResolver()

    def resolve(self, configPath: Path, baseDir: Path, level=1) -> List[Dict]:
        yamlConfig = self.__configLoader.load(configPath)
        configPaths = [{'path': configPath, 'level': level}]

        if yamlConfig is None:
            return []

        if 'imports' in yamlConfig:
            newConfigPaths = []

            for importDefinition in yamlConfig['imports']:
                newConfigPaths += self.__importDefinitionResolver.resolve(importDefinition, baseDir)

            for newConfigPath in newConfigPaths:
                configPaths += self.resolve(newConfigPath, baseDir, level + 1)

        return configPaths
