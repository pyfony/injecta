import unittest
from injecta.generator.Tag2ServicesPreparer import Tag2ServicesPreparer
from injecta.service.Service import Service
from injecta.service.argument.PrimitiveArgument import PrimitiveArgument
from injecta.dtype.DType import DType

class Tag2ServicesPreparerTest(unittest.TestCase):

    def setUp(self):
        self.__tag2ServicesPreparer = Tag2ServicesPreparer()

    def test_multilineScript(self):
        d1 = Service('foo.Bar', DType('foo.Bar', 'Bar'), [PrimitiveArgument('ahoj'), PrimitiveArgument(52)], ['console.command'])
        d2 = Service('hello.World_service', DType('hello.World', 'World'), [], ['my.tag'])
        d3 = Service('my.Name', DType('my.Name', 'Name'), [], ['console.command'])
        
        result = self.__tag2ServicesPreparer.prepare([d1, d2, d3])

        expected = {
            'console.command': [d1, d3],
            'my.tag': [d2]
        }

        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
