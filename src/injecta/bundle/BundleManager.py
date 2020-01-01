from typing import List
from box import Box
from injecta.bundle.Bundle import Bundle
from injecta.compiler.CompilerPassInterface import CompilerPassInterface
from injecta.definition.Definition import Definition

class BundleManager:

    def __init__(self, bundles: List[Bundle]):
        self.__bundles = bundles

    def getCompilerPasses(self) -> List[CompilerPassInterface]:
        compilerPasses = []

        for bundle in self.__bundles:
            compilerPasses += bundle.getCompilerPasses()

        return compilerPasses

    def modifyDefinitions(self, definitions: List[Definition]):
        for bundle in self.__bundles:
            definitions = bundle.modifyDefinitions(definitions)

        return definitions

    def modifyRawConfig(self, rawConfig: dict) -> dict:
        for bundle in self.__bundles:
            rawConfig = bundle.modifyRawConfig(rawConfig)

        return rawConfig

    def modifyParameters(self, parameters: Box) -> Box:
        for bundle in self.__bundles:
            parameters = bundle.modifyParameters(parameters)

        return parameters
