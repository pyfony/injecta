from typing import List
from injecta.definition.DefinitionParser import DefinitionParser
from injecta.definition.Definition import Definition
from injecta.schema.SchemaValidator import SchemaValidator

class DefinitionsPreparer:

    def __init__(
        self,
        schemaValidator: SchemaValidator,
        definitionParser: DefinitionParser,
    ):
        self.__schemaValidator = schemaValidator
        self.__definitionParser = definitionParser

    def prepare(self, rawServices) -> List[Definition]:
        self.__schemaValidator.validate(rawServices)

        return list(self.__definitionParser.parse(name, definition) for name, definition in rawServices.items())
