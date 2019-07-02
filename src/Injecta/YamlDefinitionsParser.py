import yaml
from Injecta.DefinitionParser import DefinitionParser

class YamlDefinitionsParser:

    def __init__(self):
        self.__definitionParser = DefinitionParser()

    def parse(self, definitionsString: str):
        if definitionsString == '':
            return []

        yamlDefinitions = yaml.safe_load(definitionsString)

        return list(self.__definitionParser.parse(name, definition) for name, definition in yamlDefinitions.items())
