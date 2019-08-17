from Injecta.Service.DefinitionParser import DefinitionParser
from Injecta.Argument.ArgumentParser import ArgumentParser
from Injecta.Module.ModuleClassResolver import ModuleClassResolver
from Injecta.Schema.SchemaValidator import SchemaValidator

class ServiceDefinitionsParser:

    def __init__(self):
        self.__definitionParser = DefinitionParser(
            ArgumentParser(),
            ModuleClassResolver()
        )
        self.__schemaValidator = SchemaValidator()

    def parse(self, rawServices: dict):
        self.__schemaValidator.validate(rawServices)

        return list(self.__definitionParser.parse(name, definition) for name, definition in rawServices.items())
