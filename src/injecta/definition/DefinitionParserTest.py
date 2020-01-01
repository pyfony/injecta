import unittest
from injecta.definition.Definition import Definition
from injecta.definition.DefinitionParser import DefinitionParser
from injecta.definition.DTypeResolver import DTypeResolver
from injecta.definition.argument.ArgumentParser import ArgumentParser
from injecta.definition.argument.PrimitiveArgument import PrimitiveArgument
from injecta.definition.argument.ServiceArgument import ServiceArgument
from injecta.dtype.DType import DType

class DefinitionParserTest(unittest.TestCase):

    def setUp(self):
        self.__definitionParser = DefinitionParser(ArgumentParser(), DTypeResolver())

    def test_serviceWithNoArgs(self):
        result = self.__definitionParser.parse('injecta.api.ApiClient.ApiClient', None)
        expected = Definition(
            'injecta.api.ApiClient.ApiClient',
            DType('injecta.api.ApiClient', 'ApiClient')
        )

        self.assertEqual(expected, result)

    def test_basic(self):
        result = self.__definitionParser.parse('injecta.api.ApiClient_test', {
            'class': 'injecta.api.ApiClient.ApiClient',
            'autowire': True,
            'arguments': [
                'Jirka',
                15,
                False,
                '@injecta.api.Connector'
            ]
        })
        expected = Definition(
            'injecta.api.ApiClient_test',
            DType('injecta.api.ApiClient', 'ApiClient'),
            [
                PrimitiveArgument('Jirka'),
                PrimitiveArgument(15),
                PrimitiveArgument(False),
                ServiceArgument('injecta.api.Connector'),
            ]
        )
        expected.setAutowire(True)

        self.assertEqual(expected, result)

    def test_factory(self):
        result = self.__definitionParser.parse('injecta.api.ApiClient', {
            'factory': ['@injecta.api.ApiClientFactory.ApiClientFactory', 'create'],
            'arguments': [
                'Jirka',
            ]
        })
        expected = Definition(
            'injecta.api.ApiClient',
            DType('injecta.api', 'ApiClient'),
            [
                PrimitiveArgument('Jirka'),
            ]
        )
        expected.setFactory(ServiceArgument('injecta.api.ApiClientFactory.ApiClientFactory'), 'create')

        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
