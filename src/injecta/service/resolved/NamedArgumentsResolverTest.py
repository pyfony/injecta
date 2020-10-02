import unittest
from injecta.dtype.DType import DType
from injecta.service.argument.PrimitiveArgument import PrimitiveArgument
from injecta.service.class_.InspectedArgumentsResolver import InspectedArgumentsResolver
from injecta.service.resolved.NamedArgumentsResolver import NamedArgumentsResolver

class NamedArgumentsResolverTest(unittest.TestCase):

    def setUp(self):
        self.__namedArgumentsResolver = NamedArgumentsResolver()
        self.__inspectedArgumentsResolver = InspectedArgumentsResolver()

    def test_basicWithDefaultValue(self):
        arguments = [
            PrimitiveArgument(111, 'numberWithDefault'),
            PrimitiveArgument('Peter', 'name'),
        ]
        inspectedArguments = self.__inspectedArgumentsResolver.resolveConstructor(DType('injecta.mocks.Bar', 'Bar'))

        resolvedArguments = self.__namedArgumentsResolver.resolve(arguments, inspectedArguments, 'injecta.mocks.Bar')

        self.assertEqual(2, len(resolvedArguments))
        self.assertEqual(PrimitiveArgument('Peter', 'name'), resolvedArguments[0].argument)
        self.assertEqual(PrimitiveArgument(111, 'numberWithDefault'), resolvedArguments[1].argument)

    def test_tooManyArguments(self):
        arguments = [
            PrimitiveArgument('Peter', 'name'),
            PrimitiveArgument(111, 'numberWithDefault'),
            PrimitiveArgument(True, 'boolWithDefault'),
            PrimitiveArgument(222, 'someNonexistentName'),
        ]
        inspectedArguments = self.__inspectedArgumentsResolver.resolveConstructor(DType('injecta.mocks.Bar', 'Bar'))

        with self.assertRaises(Exception) as error:
            self.__namedArgumentsResolver.resolve(arguments, inspectedArguments, 'injecta.mocks.Bar')

        self.assertEqual('Unknown argument "someNonexistentName" in service "injecta.mocks.Bar"', str(error.exception))

    def test_args(self):
        arguments = [
            PrimitiveArgument('George', 'name'),
        ]
        inspectedArguments = self.__inspectedArgumentsResolver.resolveConstructor(DType('injecta.mocks.Args', 'Args'))

        resolvedArguments = self.__namedArgumentsResolver.resolve(arguments, inspectedArguments, 'injecta.mocks.Args')

        self.assertEqual(1, len(resolvedArguments))
        self.assertEqual(PrimitiveArgument('George', 'name'), resolvedArguments[0].argument)

    def test_kwargs(self):
        arguments = [
            PrimitiveArgument(111, 'someNumber'),
            PrimitiveArgument('George', 'name'),
            PrimitiveArgument(True, 'someBool'),
        ]
        inspectedArguments = self.__inspectedArgumentsResolver.resolveConstructor(DType('injecta.mocks.Kwargs', 'Kwargs'))

        resolvedArguments = self.__namedArgumentsResolver.resolve(arguments, inspectedArguments, 'injecta.mocks.Kwargs')

        self.assertEqual(3, len(resolvedArguments))
        self.assertEqual(PrimitiveArgument('George', 'name'), resolvedArguments[0].argument)
        self.assertEqual(PrimitiveArgument(111, 'someNumber'), resolvedArguments[1].argument)
        self.assertEqual(PrimitiveArgument(True, 'someBool'), resolvedArguments[2].argument)

    def test_argsKwargs(self):
        arguments = [
            PrimitiveArgument(111, 'someNumber'),
            PrimitiveArgument('George', 'name'),
            PrimitiveArgument(True, 'someBool'),
        ]
        inspectedArguments = self.__inspectedArgumentsResolver.resolveConstructor(DType('injecta.mocks.ArgsKwargs', 'ArgsKwargs'))

        resolvedArguments = self.__namedArgumentsResolver.resolve(arguments, inspectedArguments, 'injecta.mocks.ArgsKwargs')

        self.assertEqual(3, len(resolvedArguments))
        self.assertEqual(PrimitiveArgument('George', 'name'), resolvedArguments[0].argument)
        self.assertEqual(PrimitiveArgument(111, 'someNumber'), resolvedArguments[1].argument)
        self.assertEqual(PrimitiveArgument(True, 'someBool'), resolvedArguments[2].argument)

if __name__ == '__main__':
    unittest.main()
