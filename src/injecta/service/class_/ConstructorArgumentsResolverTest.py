import unittest
from injecta.service.class_.ConstructorArgument import ConstructorArgument
from injecta.service.class_.ConstructorArgumentsResolver import ConstructorArgumentsResolver
from injecta.dtype.ListType import ListType
from injecta.dtype.DType import DType

class ConstructorArgumentsResolverTest(unittest.TestCase):

    def setUp(self):
        self.__constructorArgumentsResolver = ConstructorArgumentsResolver()

    def test_emptyClass(self):
        result = self.__constructorArgumentsResolver.resolve(DType('injecta.mocks.Empty', 'Empty'))

        self.assertEqual([], result)

    def test_basicClass(self):
        result = self.__constructorArgumentsResolver.resolve(DType('injecta.mocks.Foo', 'Foo'))

        expectedResult = [
            ConstructorArgument('bar', DType('injecta.mocks.Bar', 'Bar'))
        ]

        self.assertEqual(expectedResult, result)

    def test_withDefaultValues(self):
        result = self.__constructorArgumentsResolver.resolve(DType('injecta.mocks.Bar', 'Bar'))

        expectedArguments = [
            ConstructorArgument('name', DType('builtins', 'str')),
            ConstructorArgument('numberWithDefault', DType('builtins', 'int'), 0),
            ConstructorArgument('boolWithDefault', DType('builtins', 'bool'), False),
        ]

        self.assertEqual(expectedArguments, result)

    def test_withObjectList(self):
        result = self.__constructorArgumentsResolver.resolve(DType('injecta.mocks.ObjectList', 'ObjectList'))

        expectedArguments = [
            ConstructorArgument('objects', ListType('injecta.mocks.Empty', 'Empty')),
            ConstructorArgument('name', DType('builtins', 'str'), 'myName'),
        ]

        self.assertEqual(expectedArguments, result)

if __name__ == '__main__':
    unittest.main()
