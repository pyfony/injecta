import unittest
from injecta.generator.Tag2DefinitionsPreparer import Tag2DefinitionsPreparer
from injecta.definition.Definition import Definition
from injecta.definition.argument.PrimitiveArgument import PrimitiveArgument
from injecta.dtype.DType import DType

class Tag2DefinitionsPreparerTest(unittest.TestCase):

    def setUp(self):
        self.__tag2DefinitionsPreparer = Tag2DefinitionsPreparer()

    def test_multilineScript(self):
        d1 = Definition('foo.Bar', DType('foo.Bar', 'Bar'), [PrimitiveArgument('ahoj'), PrimitiveArgument(52)], ['console.command'])
        d2 = Definition('hello.World_service', DType('hello.World', 'World'), [], ['my.tag'])
        d3 = Definition('my.Name', DType('my.Name', 'Name'), [], ['console.command'])
        
        result = self.__tag2DefinitionsPreparer.prepare([d1, d2, d3])

        expected = {
            'console.command': [d1, d3],
            'my.tag': [d2]
        }

        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
