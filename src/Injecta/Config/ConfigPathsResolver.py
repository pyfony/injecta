from Injecta.Config.ConfigLoader import ConfigLoader
from Injecta.Config.ImportDefinitionResolver import ImportDefinitionResolver
from pathlib import Path

class ConfigPathsResolver:

    def __init__(self):
        self.__configLoader = ConfigLoader()
        self.__importDefinitionResolver = ImportDefinitionResolver()

    def resolve(self, configPath: Path, baseDir: Path) -> set:
        yamlConfig = self.__configLoader.load(configPath)
        configPaths = {configPath}

        if yamlConfig is None:
            return set()

        if 'imports' in yamlConfig:
            newConfigPaths = set()

            for importDefinition in yamlConfig['imports']:
                newConfigPaths = newConfigPaths.union(self.__importDefinitionResolver.resolve(importDefinition, baseDir))

            for newConfigPath in newConfigPaths:
                configPaths = configPaths.union(self.resolve(newConfigPath, baseDir))

        return set(configPaths)
