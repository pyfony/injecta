import unittest
from injecta.service.Service import Service
from injecta.service.parser.ServiceParser import ServiceParser
from injecta.service.parser.DTypeResolver import DTypeResolver
from injecta.service.argument.ArgumentParser import ArgumentParser
from injecta.service.argument.PrimitiveArgument import PrimitiveArgument
from injecta.service.argument.ServiceArgument import ServiceArgument
from injecta.dtype.DType import DType

class ServiceParserTest(unittest.TestCase):

    def setUp(self):
        self.__serviceParser = ServiceParser(ArgumentParser(), DTypeResolver())

    def test_serviceWithNoArgs(self):
        result = self.__serviceParser.parse('injecta.api.ApiClient.ApiClient', None)
        expected = Service(
            'injecta.api.ApiClient.ApiClient',
            DType('injecta.api.ApiClient', 'ApiClient')
        )

        self.assertEqual(expected, result)

    def test_basic(self):
        result = self.__serviceParser.parse('injecta.api.ApiClient_test', {
            'class': 'injecta.api.ApiClient.ApiClient',
            'autowire': True,
            'arguments': [
                'Jirka',
                15,
                False,
                '@injecta.api.Connector'
            ]
        })
        expected = Service(
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
        result = self.__serviceParser.parse('injecta.api.ApiClient', {
            'factory': ['@injecta.api.ApiClientFactory.ApiClientFactory', 'create'],
            'arguments': [
                'Jirka',
            ]
        })
        expected = Service(
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
