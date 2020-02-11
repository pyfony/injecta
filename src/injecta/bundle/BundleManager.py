from pathlib import Path
from typing import List
from box import Box
from injecta.bundle.Bundle import Bundle
from injecta.compiler.CompilerPassInterface import CompilerPassInterface
from injecta.config.ConfigLoader import ConfigLoader
from injecta.config.ConfigMerger import ConfigMerger
from injecta.definition.Definition import Definition
import importlib.util

class BundleManager:

    def __init__(self, bundles: List[Bundle]):
        self.__bundles = bundles
        self.__configLoader = ConfigLoader()
        self.__configMerger = ConfigMerger()

    def getCompilerPasses(self) -> List[CompilerPassInterface]:
        compilerPasses = []

        for bundle in self.__bundles:
            compilerPasses += bundle.getCompilerPasses()

        return compilerPasses

    def mergeRawConfig(self, appRawConfig: dict) -> dict:
        config = dict()

        for bundle in self.__bundles:
            rootModuleName = bundle.__module__[:bundle.__module__.find('.')]
            baseModuleSpec = importlib.util.find_spec(rootModuleName)
            configBasePath = baseModuleSpec.submodule_search_locations._path[0] + '/_config' # pylint: disable = protected-access

            configFileNames = bundle.getConfigFiles()

            for configFileName in configFileNames:
                configFilePath = Path(configBasePath + '/' + configFileName)
                newConfig = self.__configLoader.load(configFilePath)

                config = self.__configMerger.merge(config, newConfig, False)

        return self.__configMerger.merge(config, appRawConfig)

    def modifyRawConfig(self, rawConfig: dict) -> dict:
        for bundle in self.__bundles:
            rawConfig = bundle.modifyRawConfig(rawConfig)

        return rawConfig

    def modifyDefinitions(self, definitions: List[Definition]):
        for bundle in self.__bundles:
            definitions = bundle.modifyDefinitions(definitions)

        return definitions

    def modifyParameters(self, parameters: Box) -> Box:
        for bundle in self.__bundles:
            parameters = bundle.modifyParameters(parameters)

        return parameters
