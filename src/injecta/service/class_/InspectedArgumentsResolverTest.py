import unittest
from injecta.service.class_.InspectedArgument import InspectedArgument
from injecta.service.class_.InspectedArgumentsResolver import InspectedArgumentsResolver
from injecta.dtype.ListType import ListType
from injecta.dtype.DType import DType

class InspectedArgumentsResolverTest(unittest.TestCase):

    def setUp(self):
        self.__inspectedArgumentsResolver = InspectedArgumentsResolver()

    def test_emptyClass(self):
        result = self.__inspectedArgumentsResolver.resolveConstructor(DType('injecta.mocks.Empty', 'Empty'))

        self.assertEqual([], result)

    def test_basicClass(self):
        result = self.__inspectedArgumentsResolver.resolveConstructor(DType('injecta.mocks.Foo', 'Foo'))

        expectedResult = [
            InspectedArgument('bar', DType('injecta.mocks.Bar', 'Bar'))
        ]

        self.assertEqual(expectedResult, result)

    def test_withDefaultValues(self):
        result = self.__inspectedArgumentsResolver.resolveConstructor(DType('injecta.mocks.Bar', 'Bar'))

        expectedArguments = [
            InspectedArgument('name', DType('builtins', 'str')),
            InspectedArgument('numberWithDefault', DType('builtins', 'int'), 0),
            InspectedArgument('boolWithDefault', DType('builtins', 'bool'), False),
        ]

        self.assertEqual(expectedArguments, result)

    def test_withDefaultNoneValue(self):
        result = self.__inspectedArgumentsResolver.resolveConstructor(DType('injecta.mocks.NoneClass', 'NoneClass'))

        expectedArguments = [
            InspectedArgument('name', DType('builtins', 'str')),
            InspectedArgument('someNoneValue', DType('builtins', 'int'), None),
        ]

        self.assertEqual(expectedArguments, result)
        self.assertTrue(result[1].hasDefaultValue())

    def test_withObjectList(self):
        result = self.__inspectedArgumentsResolver.resolveConstructor(DType('injecta.mocks.ObjectList', 'ObjectList'))

        expectedArguments = [
            InspectedArgument('objects', ListType('injecta.mocks.Empty', 'Empty')),
            InspectedArgument('name', DType('builtins', 'str'), 'myName'),
        ]

        self.assertEqual(expectedArguments, result)

    def test_useParentConstructor(self):
        result = self.__inspectedArgumentsResolver.resolveConstructor(DType('injecta.mocks.UseParentConstructor', 'UseParentConstructor'))

        expectedArguments = [
            InspectedArgument('name', DType('builtins', 'str')),
            InspectedArgument('numberWithDefault', DType('builtins', 'int'), 0),
            InspectedArgument('boolWithDefault', DType('builtins', 'bool'), False),
        ]

        self.assertEqual(expectedArguments, result)

if __name__ == '__main__':
    unittest.main()
