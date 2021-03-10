import unittest
from injecta.service.ServiceAlias import ServiceAlias
from injecta.service.parser.ServiceParser import ServiceParser
from injecta.service.parser.ServicesPreparer import ServicesPreparer
from injecta.service.parser.DTypeResolver import DTypeResolver
from injecta.service.argument.ArgumentParser import ArgumentParser
from injecta.schema.SchemaValidator import SchemaValidator
from injecta.dtype.DType import DType
from injecta.service.argument.PrimitiveArgument import PrimitiveArgument
from injecta.service.argument.ServiceArgument import ServiceArgument
from injecta.service.Service import Service


class ServicesPreparerTest(unittest.TestCase):
    def setUp(self):
        self.__services_preparer = ServicesPreparer(
            SchemaValidator(),
            ServiceParser(
                ArgumentParser(),
                DTypeResolver(),
            ),
        )

    def test_basic(self):
        raw_services = {
            "injecta.mocks.Bar.Bar": {"arguments": ["Jiri Koutny"]},
            "injecta.mocks.Foo.Foo": {"arguments": ["@injecta.mocks.Bar.Bar"]},
            "injecta.mocks.Bar.BarAlias": "@injecta.mocks.Bar.Bar",
        }

        expected_service1 = Service(
            "injecta.mocks.Bar.Bar",
            DType("injecta.mocks.Bar", "Bar"),
            [
                PrimitiveArgument("Jiri Koutny"),
            ],
        )

        expected_service2 = Service(
            "injecta.mocks.Foo.Foo",
            DType("injecta.mocks.Foo", "Foo"),
            [
                ServiceArgument("injecta.mocks.Bar.Bar"),
            ],
        )

        expected_alias1 = ServiceAlias("injecta.mocks.Bar.BarAlias", "injecta.mocks.Bar.Bar")

        services, aliases = self.__services_preparer.prepare(raw_services)

        self.assertEqual(expected_service1, services[0])
        self.assertEqual(expected_service2, services[1])
        self.assertEqual(expected_alias1, aliases[0])


if __name__ == "__main__":
    unittest.main()
