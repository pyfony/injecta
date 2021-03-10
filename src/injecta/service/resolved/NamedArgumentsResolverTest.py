import unittest
from injecta.dtype.DType import DType
from injecta.service.argument.PrimitiveArgument import PrimitiveArgument
from injecta.service.class_.InspectedArgumentsResolver import InspectedArgumentsResolver
from injecta.service.resolved.NamedArgumentsResolver import NamedArgumentsResolver


class NamedArgumentsResolverTest(unittest.TestCase):
    def setUp(self):
        self.__named_arguments_resolver = NamedArgumentsResolver()
        self.__inspected_arguments_resolver = InspectedArgumentsResolver()

    def test_basic_with_default_value(self):
        arguments = [
            PrimitiveArgument(111, "number_with_default"),
            PrimitiveArgument("Peter", "name"),
        ]
        inspected_arguments = self.__inspected_arguments_resolver.resolve_constructor(DType("injecta.mocks.Bar", "Bar"))

        resolved_arguments = self.__named_arguments_resolver.resolve(arguments, inspected_arguments, "injecta.mocks.Bar")

        self.assertEqual(2, len(resolved_arguments))
        self.assertEqual(PrimitiveArgument("Peter", "name"), resolved_arguments[0].argument)
        self.assertEqual(PrimitiveArgument(111, "number_with_default"), resolved_arguments[1].argument)

    def test_too_many_arguments(self):
        arguments = [
            PrimitiveArgument("Peter", "name"),
            PrimitiveArgument(111, "number_with_default"),
            PrimitiveArgument(True, "bool_with_default"),
            PrimitiveArgument(222, "some_nonexistent_name"),
        ]
        inspected_arguments = self.__inspected_arguments_resolver.resolve_constructor(DType("injecta.mocks.Bar", "Bar"))

        with self.assertRaises(Exception) as error:
            self.__named_arguments_resolver.resolve(arguments, inspected_arguments, "injecta.mocks.Bar")

        self.assertEqual('Unknown argument "some_nonexistent_name" in service "injecta.mocks.Bar"', str(error.exception))

    def test_args(self):
        arguments = [
            PrimitiveArgument("George", "name"),
        ]
        inspected_arguments = self.__inspected_arguments_resolver.resolve_constructor(DType("injecta.mocks.Args", "Args"))

        resolved_arguments = self.__named_arguments_resolver.resolve(arguments, inspected_arguments, "injecta.mocks.Args")

        self.assertEqual(1, len(resolved_arguments))
        self.assertEqual(PrimitiveArgument("George", "name"), resolved_arguments[0].argument)

    def test_kwargs(self):
        arguments = [
            PrimitiveArgument(111, "some_number"),
            PrimitiveArgument("George", "name"),
            PrimitiveArgument(True, "some_bool"),
        ]
        inspected_arguments = self.__inspected_arguments_resolver.resolve_constructor(DType("injecta.mocks.Kwargs", "Kwargs"))

        resolved_arguments = self.__named_arguments_resolver.resolve(arguments, inspected_arguments, "injecta.mocks.Kwargs")

        self.assertEqual(3, len(resolved_arguments))
        self.assertEqual(PrimitiveArgument("George", "name"), resolved_arguments[0].argument)
        self.assertEqual(PrimitiveArgument(111, "some_number"), resolved_arguments[1].argument)
        self.assertEqual(PrimitiveArgument(True, "some_bool"), resolved_arguments[2].argument)

    def test_args_kwargs(self):
        arguments = [
            PrimitiveArgument(111, "some_number"),
            PrimitiveArgument("George", "name"),
            PrimitiveArgument(True, "some_bool"),
        ]
        inspected_arguments = self.__inspected_arguments_resolver.resolve_constructor(DType("injecta.mocks.ArgsKwargs", "ArgsKwargs"))

        resolved_arguments = self.__named_arguments_resolver.resolve(arguments, inspected_arguments, "injecta.mocks.ArgsKwargs")

        self.assertEqual(3, len(resolved_arguments))
        self.assertEqual(PrimitiveArgument("George", "name"), resolved_arguments[0].argument)
        self.assertEqual(PrimitiveArgument(111, "some_number"), resolved_arguments[1].argument)
        self.assertEqual(PrimitiveArgument(True, "some_bool"), resolved_arguments[2].argument)


if __name__ == "__main__":
    unittest.main()
