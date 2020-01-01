from injecta.definition.DefinitionParser import DefinitionParser
from injecta.definition.DefinitionsPreparer import DefinitionsPreparer
from injecta.definition.DTypeResolver import DTypeResolver
from injecta.definition.argument.ArgumentParser import ArgumentParser
from injecta.schema.SchemaValidator import SchemaValidator

def create():
    return DefinitionsPreparer(
        SchemaValidator(),
        DefinitionParser(
            ArgumentParser(),
            DTypeResolver(),
        )
    )
