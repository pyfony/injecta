import unittest
from injecta.dtype.DType import DType
from injecta.service.argument.PrimitiveArgument import PrimitiveArgument
from injecta.service.class_.InspectedArgumentsResolver import InspectedArgumentsResolver
from injecta.service.resolved.ArgumentListResolver import ArgumentListResolver

class ArgumentListResolverTest(unittest.TestCase):

    def setUp(self):
        self.__argumentListResolver = ArgumentListResolver()
        self.__inspectedArgumentsResolver = InspectedArgumentsResolver()

    def test_basicWithDefaultValue(self):
        arguments = [
            PrimitiveArgument('Peter'),
            PrimitiveArgument(111),
        ]
        inspectedArguments = self.__inspectedArgumentsResolver.resolveConstructor(DType('injecta.mocks.Bar', 'Bar'))

        resolvedArguments = self.__argumentListResolver.resolve(arguments, inspectedArguments, 'injecta.mocks.Bar')

        self.assertEqual(2, len(resolvedArguments))
        self.assertEqual(PrimitiveArgument('Peter'), resolvedArguments[0].argument)
        self.assertEqual(PrimitiveArgument(111), resolvedArguments[1].argument)

    def test_tooManyArguments(self):
        arguments = [
            PrimitiveArgument('Peter'),
            PrimitiveArgument(111),
            PrimitiveArgument(True),
            PrimitiveArgument(222),
        ]
        inspectedArguments = self.__inspectedArgumentsResolver.resolveConstructor(DType('injecta.mocks.Bar', 'Bar'))

        with self.assertRaises(Exception) as error:
            self.__argumentListResolver.resolve(arguments, inspectedArguments, 'injecta.mocks.Bar')

        self.assertEqual('Too many arguments given for "injecta.mocks.Bar"', str(error.exception))

    def test_args(self):
        arguments = [
            PrimitiveArgument('Peter'),
            PrimitiveArgument(111),
        ]
        inspectedArguments = self.__inspectedArgumentsResolver.resolveConstructor(DType('injecta.mocks.Args', 'Args'))

        resolvedArguments = self.__argumentListResolver.resolve(arguments, inspectedArguments, 'injecta.mocks.Args')

        self.assertEqual(2, len(resolvedArguments))
        self.assertEqual(PrimitiveArgument('Peter'), resolvedArguments[0].argument)
        self.assertEqual(PrimitiveArgument(111), resolvedArguments[1].argument)

    def test_kwargs(self):
        arguments = []
        inspectedArguments = self.__inspectedArgumentsResolver.resolveConstructor(DType('injecta.mocks.Kwargs', 'Kwargs'))

        with self.assertRaises(Exception) as error:
            self.__argumentListResolver.resolve(arguments, inspectedArguments, 'injecta.mocks.Kwargs')

        self.assertEqual('__init__() in service "injecta.mocks.Kwargs" contains **kwargs, use named arguments instead', str(error.exception))

    def test_argsKwargs(self):
        arguments = []
        inspectedArguments = self.__inspectedArgumentsResolver.resolveConstructor(DType('injecta.mocks.ArgsKwargs', 'ArgsKwargs'))

        with self.assertRaises(Exception) as error:
            self.__argumentListResolver.resolve(arguments, inspectedArguments, 'injecta.mocks.ArgsKwargs')

        self.assertEqual('__init__() in service "injecta.mocks.ArgsKwargs" contains **kwargs, use named arguments instead', str(error.exception))

if __name__ == '__main__':
    unittest.main()
