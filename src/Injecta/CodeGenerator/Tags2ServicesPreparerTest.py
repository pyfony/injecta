import unittest

from Injecta.CodeGenerator.Tags2ServicesPreparer import Tags2ServicesPreparer
from Injecta.Service.Definition import Definition

class LinesTransformerTest(unittest.TestCase):

    def setUp(self):
        self.__tags2ServicesPreparer = Tags2ServicesPreparer()

    def test_multilineScript(self):
        d1 = Definition('Foo.Bar', 'Foo.Bar', ['ahoj', 52], ['console.command'])
        d2 = Definition('Hello.World_ping', 'Hello.World', [], ['my.tag'])
        d3 = Definition('My.Name', 'My.Name', [], ['console.command'])
        
        result = self.__tags2ServicesPreparer.prepare([d1, d2, d3])

        expected = {
            'console.command': ['Foo.Bar', 'My.Name'],
            'my.tag': ['Hello.World_ping']
        }

        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
