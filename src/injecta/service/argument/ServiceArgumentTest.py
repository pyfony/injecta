import unittest
from injecta.dtype.DType import DType
from injecta.service.argument.ServiceArgument import ServiceArgument
from injecta.service.class_.InspectedArgument import InspectedArgument


class ServiceArgumentTest(unittest.TestCase):
    def test_basic(self):
        service_argument = ServiceArgument("foo.Bar")
        inspected_argument = InspectedArgument("bar", DType("foo.Bar", "Bar"))
        services2_classes = {"foo.Bar": DType("foo.Bar", "Bar")}
        aliases2_services = {}

        service_argument.check_type_matches_definition(inspected_argument, services2_classes, aliases2_services)

    def test_aliased(self):
        service_argument = ServiceArgument("foo.BarAlias")
        inspected_argument = InspectedArgument("bar", DType("foo.Bar", "Bar"))
        services2_classes = {"foo.Bar": DType("foo.Bar", "Bar")}
        aliases2_services = {"foo.BarAlias": "foo.Bar"}

        service_argument.check_type_matches_definition(inspected_argument, services2_classes, aliases2_services)

    def test_undefined_service(self):
        service_argument = ServiceArgument("foo.Bar")
        inspected_argument = InspectedArgument("bar", DType("foo.Bar", "Bar"))
        services2_classes = {}
        aliases2_services = {}

        with self.assertRaises(Exception) as error:
            service_argument.check_type_matches_definition(inspected_argument, services2_classes, aliases2_services)

        self.assertEqual("Undefined service foo.Bar", str(error.exception))

    def test_unknown_aliased_service(self):
        service_argument = ServiceArgument("foo.BarAlias")
        inspected_argument = InspectedArgument("bar", DType("foo.Bar", "Bar"))
        services2_classes = {}
        aliases2_services = {"foo.BarAlias": "foo.Bar"}

        with self.assertRaises(Exception) as error:
            service_argument.check_type_matches_definition(inspected_argument, services2_classes, aliases2_services)

        self.assertEqual('Aliased service "foo.Bar" does not exist', str(error.exception))

    def test_interface(self):
        service_argument = ServiceArgument("injecta.mocks.Bar")
        inspected_argument = InspectedArgument("bar", DType("injecta.mocks.BarInterface", "BarInterface"))
        services2_classes = {"injecta.mocks.Bar": DType("injecta.mocks.Bar", "Bar")}
        aliases2_services = {}

        service_argument.check_type_matches_definition(inspected_argument, services2_classes, aliases2_services)


if __name__ == "__main__":
    unittest.main()
