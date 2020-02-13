import unittest
from injecta.parameter.PlaceholderReplacer import PlaceholderReplacer
import os

class PlaceholderReplacerTest(unittest.TestCase):

    def setUp(self):
        self.__placeholderReplacer = PlaceholderReplacer()

    def test_basicMultiLevel(self):
        result = self.__placeholderReplacer.replace({
            'level_1': '1',
            'level_2_1': '2 + %level_1%',
            'level_3_2_1': '3 + %level_2_1%',
            'level_4_3_2_1': '4 + %level_3_2_1%',
        })

        self.assertEqual('1', result['level_1'])
        self.assertEqual('2 + 1', result['level_2_1'])
        self.assertEqual('3 + 2 + 1', result['level_3_2_1'])
        self.assertEqual('4 + 3 + 2 + 1', result['level_4_3_2_1'])

    def test_multiplePlaceholders(self):
        result = self.__placeholderReplacer.replace({
            'level_1': '1',
            'level_2_1': '2 + %level_1%',
            'level_3': '3',
            'level_4_3_2_1': '4 + %level_3% + %level_2_1%',
        })

        self.assertEqual('1', result['level_1'])
        self.assertEqual('2 + 1', result['level_2_1'])
        self.assertEqual('4 + 3 + 2 + 1', result['level_4_3_2_1'])

    def test_typesConsistency(self):
        result = self.__placeholderReplacer.replace({
            'typedValues': {
                'number': 123456,
                'bool': True,
                'none': None,
            },
            'referencedTypedValues': {
                'number': '%typedValues.number%',
                'bool': '%typedValues.bool%',
                'none': '%typedValues.none%',
            },
        })

        self.assertEqual(123456, result['referencedTypedValues']['number'])
        self.assertEqual(True, result['referencedTypedValues']['bool'])
        self.assertEqual(None, result['referencedTypedValues']['none'])

    def test_envVariables(self):
        os.environ['LEVEL_1'] = '1'

        result = self.__placeholderReplacer.replace({
            'level_2_1': '2 + %env(LEVEL_1)%',
            'level_3_2_1': '3 + %level_2_1%',
            'level_4_3_2_1': '4 + %level_3_2_1%',
        })

        self.assertEqual('2 + 1', result['level_2_1'])
        self.assertEqual('3 + 2 + 1', result['level_3_2_1'])
        self.assertEqual('4 + 3 + 2 + 1', result['level_4_3_2_1'])

    def test_full(self):
        os.environ['APP_ENV'] = 'dev'

        result = self.__placeholderReplacer.replace({
            'first': {
                'second': {
                    'third': 52,
                }
            },
            'myList': ['/foo/bar', '%projectRoot%/ahoj/svete/%first.second.third%', '%project.rootPath%/ahoj/svete'],
            'paths': {
                'partiesPath': '/foo/bar',
                'ordersPath': '%projectRoot%/ahoj/svete/%first.second.third%',
                'projectsPath': '%project.rootPath%/ahoj/svete'
            },
            'projectRoot': '/%env(APP_ENV)%/myroot',
            'project': {
                'rootPath': '/project_root_path',
            },
            'myListLinked': '%myList%',
            'myDictLinked': '%paths%',
        })

        self.assertEqual('/dev/myroot/ahoj/svete/52', result['paths']['ordersPath'])
        self.assertEqual('/project_root_path/ahoj/svete', result['paths']['projectsPath'])
        self.assertEqual('/foo/bar', result['myList'][0])
        self.assertEqual('/dev/myroot/ahoj/svete/52', result['myList'][1])
        self.assertEqual('/dev/myroot/ahoj/svete/52', result['myListLinked'][1])
        self.assertEqual('/project_root_path/ahoj/svete', result['myDictLinked']['projectsPath'])

    def test_non_existing(self):
        with self.assertRaises(Exception) as cm:
            self.__placeholderReplacer.replace({
                'first': {
                    'second': {
                        'third': '52'
                    }
                },
                'paths': {
                    'ordersPath': 'ahoj/%first.second.thirdddddd%',
                }
            })

            self.assertEqual('parameter "first.second.thirdddddd" not found', cm.exception.msg)

if __name__ == '__main__':
    unittest.main()
