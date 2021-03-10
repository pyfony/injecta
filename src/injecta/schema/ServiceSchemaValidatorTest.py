import unittest
from injecta.schema.ServiceSchemaValidator import ServiceSchemaValidator
from injecta.schema.SchemaValidationException import SchemaValidationException


class ServiceSchemaValidatorTest(unittest.TestCase):
    def setUp(self):
        self.__schema_validator = ServiceSchemaValidator()

    def test_basic(self):
        self.__schema_validator.validate("Foo.Bar", None)

    def test_basic_fail(self):
        with self.assertRaises(SchemaValidationException) as error:
            self.__schema_validator.validate("Foo.Bar", 1)

        self.assertEqual('service "Foo.Bar" not properly defined', str(error.exception))

    def test_basic_arguments_without_key(self):
        raw_service_definition = ["jirka", 1]

        with self.assertRaises(SchemaValidationException) as error:
            self.__schema_validator.validate("Foo.Bar", raw_service_definition)

        self.assertEqual('Arguments of service "Foo.Bar" must be defined in the "arguments" key', str(error.exception))

    def test_unexpected_attribute(self):
        raw_service_definition = {"arguments": ["jirka", 1], "banana": True}

        with self.assertRaises(SchemaValidationException) as error:
            self.__schema_validator.validate("Foo.Bar", raw_service_definition)

        self.assertEqual('Unexpected attributes (banana) for service "Foo.Bar"', str(error.exception))

    def test_invalid_alias(self):
        raw_service_definition = "mycompany.MyService"

        with self.assertRaises(SchemaValidationException) as error:
            self.__schema_validator.validate("mycompany.MyServiceAlias", raw_service_definition)

        self.assertEqual("Service aliased with mycompany.MyServiceAlias must be prefixed with @", str(error.exception))

    def test_autowire(self):
        raw_service_definition = {"arguments": ["jirka", 1], "autowire": 1}

        with self.assertRaises(SchemaValidationException) as error:
            self.__schema_validator.validate("Foo.Bar", raw_service_definition)

        self.assertEqual('Attribute "autowire" of service "Foo.Bar" must be True or False', str(error.exception))

    def test_factory(self):
        raw_service_definition = {"arguments": ["jirka", 1], "factory": "Foo.BarFactory:create"}

        with self.assertRaises(SchemaValidationException) as error:
            self.__schema_validator.validate("Foo.Bar", raw_service_definition)

        self.assertEqual('Attribute "factory" of service "Foo.Bar" must be list [factory_class, factory_method]', str(error.exception))

    def test_full_ok(self):
        raw_service_definition = {
            "arguments": ["jirka", 1],
            "tags": ["console.command"],
            "autowire": True,
            "factory": ["@Foo.BarFactory", "create"],
        }

        self.__schema_validator.validate("Foo.Bar", raw_service_definition)


if __name__ == "__main__":
    unittest.main()
