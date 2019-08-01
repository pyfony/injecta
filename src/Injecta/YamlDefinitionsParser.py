import yaml
from Injecta.DefinitionParser import DefinitionParser
from Injecta.Argument.ArgumentParser import ArgumentParser
from Injecta.Module.ModuleClassResolver import ModuleClassResolver
from Injecta.Schema.SchemaValidator import SchemaValidator

class YamlDefinitionsParser:

    def __init__(self):
        self.__definitionParser = DefinitionParser(
            ArgumentParser(),
            ModuleClassResolver()
        )
        self.__schemaValidator = SchemaValidator()

    def parse(self, definitionsString: str):
        if definitionsString == '':
            return []

        yamlDefinitions = yaml.safe_load(definitionsString)

        self.__schemaValidator.validate(yamlDefinitions)

        return list(self.__definitionParser.parse(name, definition) for name, definition in yamlDefinitions.items())
