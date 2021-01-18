import unittest
from injecta.schema.ServiceSchemaValidator import ServiceSchemaValidator
from injecta.schema.SchemaValidationException import SchemaValidationException

class ServiceSchemaValidatorTest(unittest.TestCase):

    def setUp(self):
        self.__schemaValidator = ServiceSchemaValidator()

    def test_basic(self):
        self.__schemaValidator.validate('Foo.Bar', None)

    def test_basic_fail(self):
        with self.assertRaises(SchemaValidationException) as error:
            self.__schemaValidator.validate('Foo.Bar', 1)

        self.assertEqual('service "Foo.Bar" not properly defined', str(error.exception))

    def test_basic_argumentsWithoutKey(self):
        rawServiceDefinition = [
            'jirka',
            1
        ]

        with self.assertRaises(SchemaValidationException) as error:
            self.__schemaValidator.validate('Foo.Bar', rawServiceDefinition)

        self.assertEqual('Arguments of service "Foo.Bar" must be defined in the "arguments" key', str(error.exception))

    def test_unexpectedAttribute(self):
        rawServiceDefinition = {
            'arguments': [
                'jirka',
                1
            ],
            'banana': True
        }

        with self.assertRaises(SchemaValidationException) as error:
            self.__schemaValidator.validate('Foo.Bar', rawServiceDefinition)

        self.assertEqual('Unexpected attributes (banana) for service "Foo.Bar"', str(error.exception))

    def test_invalidAlias(self):
        rawServiceDefinition = 'mycompany.MyService'

        with self.assertRaises(SchemaValidationException) as error:
            self.__schemaValidator.validate('mycompany.MyServiceAlias', rawServiceDefinition)

        self.assertEqual('Service aliased with mycompany.MyServiceAlias must be prefixed with @', str(error.exception))

    def test_autowire(self):
        rawServiceDefinition = {
            'arguments': [
                'jirka',
                1
            ],
            'autowire': 1
        }

        with self.assertRaises(SchemaValidationException) as error:
            self.__schemaValidator.validate('Foo.Bar', rawServiceDefinition)

        self.assertEqual('Attribute "autowire" of service "Foo.Bar" must be True or False', str(error.exception))

    def test_factory(self):
        rawServiceDefinition = {
            'arguments': [
                'jirka',
                1
            ],
            'factory': 'Foo.BarFactory:create'
        }

        with self.assertRaises(SchemaValidationException) as error:
            self.__schemaValidator.validate('Foo.Bar', rawServiceDefinition)

        self.assertEqual('Attribute "factory" of service "Foo.Bar" must be list [factoryClass, factoryMethod]', str(error.exception))

    def test_fullOk(self):
        rawServiceDefinition = {
            'arguments': [
                'jirka',
                1
            ],
            'tags': ['console.command'],
            'autowire': True,
            'factory': ['@Foo.BarFactory', 'create']
        }

        self.__schemaValidator.validate('Foo.Bar', rawServiceDefinition)

if __name__ == '__main__':
    unittest.main()
