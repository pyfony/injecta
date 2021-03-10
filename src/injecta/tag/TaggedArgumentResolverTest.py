import unittest
from injecta.container.ContainerBuild import ContainerBuild
from injecta.dtype.DType import DType
from injecta.service.Service import Service
from injecta.service.argument.ListArgument import ListArgument
from injecta.service.argument.PrimitiveArgument import PrimitiveArgument
from injecta.service.argument.TaggedServicesArgument import TaggedServicesArgument
from injecta.service.class_.InspectedArgument import InspectedArgument
from injecta.service.resolved.ResolvedArgument import ResolvedArgument
from injecta.tag.TaggedArgumentResolver import TaggedArgumentResolver


class TaggedArgumentResolverTest(unittest.TestCase):
    def setUp(self):
        self.__tagged_argument_resolver = TaggedArgumentResolver()

    def test_no_change(self):
        resolved_argument = ResolvedArgument("my_number", PrimitiveArgument(123), InspectedArgument("my_number", DType("builtins", "int")))
        container_build = ContainerBuild({}, [], {}, {}, {})

        new_resolved_argument = self.__tagged_argument_resolver.resolve(resolved_argument, container_build)

        self.assertEqual(resolved_argument, new_resolved_argument)

    def test_basic(self):
        resolved_argument = ResolvedArgument(
            "my_number", TaggedServicesArgument("my_service_tag"), InspectedArgument("my_tagged_services", DType("builtins", "list"))
        )

        new_resolved_argument = self.__tagged_argument_resolver.resolve(resolved_argument, self.__create_container_build())

        list_argument = new_resolved_argument.argument

        self.assertIsInstance(list_argument, ListArgument)
        self.assertEqual(None, list_argument.name)
        self.assertEqual("injecta.mocks.Bar", list_argument.items[0].service_name)
        self.assertEqual("injecta.mocks.Bar.new", list_argument.items[1].service_name)

    def test_named_argument(self):
        resolved_argument = ResolvedArgument(
            "my_number",
            TaggedServicesArgument("my_service_tag", "my_tagged_services"),
            InspectedArgument("my_tagged_services", DType("builtins", "list")),
        )

        new_resolved_argument = self.__tagged_argument_resolver.resolve(resolved_argument, self.__create_container_build())

        list_argument = new_resolved_argument.argument

        self.assertIsInstance(list_argument, ListArgument)
        self.assertEqual("my_tagged_services", list_argument.name)
        self.assertEqual("injecta.mocks.Bar", list_argument.items[0].service_name)
        self.assertEqual("injecta.mocks.Bar.new", list_argument.items[1].service_name)

    def __create_container_build(self):
        tags2_services = {
            "my_service_tag": [
                Service("injecta.mocks.Bar", DType("injecta.mocks.Bar", "Bar")),
                Service("injecta.mocks.Bar.new", DType("injecta.mocks.Bar", "Bar")),
            ]
        }

        return ContainerBuild({}, [], {}, {}, tags2_services)


if __name__ == "__main__":
    unittest.main()
