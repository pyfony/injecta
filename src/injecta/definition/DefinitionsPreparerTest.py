import unittest
from injecta.definition.DefinitionParser import DefinitionParser
from injecta.definition.DefinitionsPreparer import DefinitionsPreparer
from injecta.definition.DTypeResolver import DTypeResolver
from injecta.definition.argument.ArgumentParser import ArgumentParser
from injecta.schema.SchemaValidator import SchemaValidator
from injecta.dtype.DType import DType
from injecta.definition.argument.PrimitiveArgument import PrimitiveArgument
from injecta.definition.argument.ServiceArgument import ServiceArgument
from injecta.definition.Definition import Definition

class DefinitionsPreparerTest(unittest.TestCase):

    def setUp(self):
        self.__definitionsPreparer = DefinitionsPreparer(
            SchemaValidator(),
            DefinitionParser(
                ArgumentParser(),
                DTypeResolver(),
            )
        )

    def test_basic(self):
        rawServices = {
            'injecta.mocks.Bar.Bar': {
                'arguments': [
                    'Jiri Koutny'
                ]
            },
            'injecta.mocks.Foo.Foo': {
                'arguments': [
                    '@injecta.mocks.Bar.Bar'
                ]
            },
        }

        expectedDefinition1 = Definition(
            'injecta.mocks.Bar.Bar',
            DType('injecta.mocks.Bar', 'Bar'),
            [
                PrimitiveArgument('Jiri Koutny'),
            ]
        )

        expectedDefinition2 = Definition(
            'injecta.mocks.Foo.Foo',
            DType('injecta.mocks.Foo', 'Foo'),
            [
                ServiceArgument('injecta.mocks.Bar.Bar'),
            ]
        )

        result = self.__definitionsPreparer.prepare(rawServices)

        self.assertEqual(expectedDefinition1, result[0])
        self.assertEqual(expectedDefinition2, result[1])

if __name__ == '__main__':
    unittest.main()
