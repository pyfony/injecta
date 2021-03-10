import unittest
from injecta.service.class_.InspectedArgument import InspectedArgument
from injecta.service.class_.InspectedArgumentsResolver import InspectedArgumentsResolver
from injecta.dtype.ListType import ListType
from injecta.dtype.DType import DType


class InspectedArgumentsResolverTest(unittest.TestCase):
    def setUp(self):
        self.__inspected_arguments_resolver = InspectedArgumentsResolver()

    def test_empty_class(self):
        result = self.__inspected_arguments_resolver.resolve_constructor(DType("injecta.mocks.Empty", "Empty"))

        self.assertEqual([], result)

    def test_basic_class(self):
        result = self.__inspected_arguments_resolver.resolve_constructor(DType("injecta.mocks.Foo", "Foo"))

        expected_result = [InspectedArgument("bar", DType("injecta.mocks.Bar", "Bar"))]

        self.assertEqual(expected_result, result)

    def test_with_default_values(self):
        result = self.__inspected_arguments_resolver.resolve_constructor(DType("injecta.mocks.Bar", "Bar"))

        expected_arguments = [
            InspectedArgument("name", DType("builtins", "str")),
            InspectedArgument("number_with_default", DType("builtins", "int"), 0),
            InspectedArgument("bool_with_default", DType("builtins", "bool"), False),
        ]

        self.assertEqual(expected_arguments, result)

    def test_with_default_none_value(self):
        result = self.__inspected_arguments_resolver.resolve_constructor(DType("injecta.mocks.NoneClass", "NoneClass"))

        expected_arguments = [
            InspectedArgument("name", DType("builtins", "str")),
            InspectedArgument("some_none_value", DType("builtins", "int"), None),
        ]

        self.assertEqual(expected_arguments, result)
        self.assertTrue(result[1].has_default_value())

    def test_with_object_list(self):
        result = self.__inspected_arguments_resolver.resolve_constructor(DType("injecta.mocks.ObjectList", "ObjectList"))

        expected_arguments = [
            InspectedArgument("objects", ListType("injecta.mocks.Empty", "Empty")),
            InspectedArgument("name", DType("builtins", "str"), "my_name"),
        ]

        self.assertEqual(expected_arguments, result)

    def test_use_parent_constructor(self):
        result = self.__inspected_arguments_resolver.resolve_constructor(
            DType("injecta.mocks.UseParentConstructor", "UseParentConstructor")
        )

        expected_arguments = [
            InspectedArgument("name", DType("builtins", "str")),
            InspectedArgument("number_with_default", DType("builtins", "int"), 0),
            InspectedArgument("bool_with_default", DType("builtins", "bool"), False),
        ]

        self.assertEqual(expected_arguments, result)


if __name__ == "__main__":
    unittest.main()
