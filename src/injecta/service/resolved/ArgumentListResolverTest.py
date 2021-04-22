import unittest
from injecta.dtype.DType import DType
from injecta.service.argument.PrimitiveArgument import PrimitiveArgument
from injecta.service.class_.InspectedArgumentsResolver import InspectedArgumentsResolver
from injecta.service.resolved.ArgumentListResolver import ArgumentListResolver


class ArgumentListResolverTest(unittest.TestCase):
    def setUp(self):
        self.__argument_list_resolver = ArgumentListResolver()
        self.__inspected_arguments_resolver = InspectedArgumentsResolver()

    def test_basic_with_default_value(self):
        arguments = [
            PrimitiveArgument("Peter"),
            PrimitiveArgument(111),
        ]
        inspected_arguments = self.__inspected_arguments_resolver.resolve_constructor(DType("injecta.mocks.Bar", "Bar"))

        resolved_arguments = self.__argument_list_resolver.resolve(arguments, inspected_arguments, "injecta.mocks.Bar")

        self.assertEqual(2, len(resolved_arguments))
        self.assertEqual(PrimitiveArgument("Peter"), resolved_arguments[0].argument)
        self.assertEqual(PrimitiveArgument(111), resolved_arguments[1].argument)

    def test_too_many_arguments(self):
        arguments = [
            PrimitiveArgument("Peter"),
            PrimitiveArgument(111),
            PrimitiveArgument(True),
            PrimitiveArgument(222),
        ]
        inspected_arguments = self.__inspected_arguments_resolver.resolve_constructor(DType("injecta.mocks.Bar", "Bar"))

        with self.assertRaises(Exception) as error:
            self.__argument_list_resolver.resolve(arguments, inspected_arguments, "injecta.mocks.Bar")

        self.assertEqual('Too many arguments given for service "injecta.mocks.Bar"', str(error.exception))

    def test_args(self):
        arguments = [
            PrimitiveArgument("Peter"),
            PrimitiveArgument(111),
        ]
        inspected_arguments = self.__inspected_arguments_resolver.resolve_constructor(DType("injecta.mocks.Args", "Args"))

        resolved_arguments = self.__argument_list_resolver.resolve(arguments, inspected_arguments, "injecta.mocks.Args")

        self.assertEqual(2, len(resolved_arguments))
        self.assertEqual(PrimitiveArgument("Peter"), resolved_arguments[0].argument)
        self.assertEqual(PrimitiveArgument(111), resolved_arguments[1].argument)

    def test_kwargs(self):
        arguments = []
        inspected_arguments = self.__inspected_arguments_resolver.resolve_constructor(DType("injecta.mocks.Kwargs", "Kwargs"))

        with self.assertRaises(Exception) as error:
            self.__argument_list_resolver.resolve(arguments, inspected_arguments, "injecta.mocks.Kwargs")

        self.assertEqual(
            '__init__() in service "injecta.mocks.Kwargs" contains **kwargs, use named arguments instead', str(error.exception)
        )

    def test_args_kwargs(self):
        arguments = []
        inspected_arguments = self.__inspected_arguments_resolver.resolve_constructor(DType("injecta.mocks.ArgsKwargs", "ArgsKwargs"))

        with self.assertRaises(Exception) as error:
            self.__argument_list_resolver.resolve(arguments, inspected_arguments, "injecta.mocks.ArgsKwargs")

        self.assertEqual(
            '__init__() in service "injecta.mocks.ArgsKwargs" contains **kwargs, use named arguments instead', str(error.exception)
        )


if __name__ == "__main__":
    unittest.main()
