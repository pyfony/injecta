import yaml
from Injecta.Definition import Definition
from Injecta.DefinitionParser import DefinitionParser

class YamlParser:

    def __init__(
        self,
        definitionParser: DefinitionParser
        ):
        self.__definitionParser = definitionParser
        
    def parse(self, content: str):
        yamlDefinitions = yaml.safe_load(content)
        definitions = []

        for serviceName, serviceDefinition in yamlDefinitions.items():
            definitions.append(self.__definitionParser.parse(serviceName, serviceDefinition))

        return definitions
