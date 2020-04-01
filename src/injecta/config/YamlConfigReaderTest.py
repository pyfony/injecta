import unittest
from injecta.config.YamlConfigReader import YamlConfigReader
from injecta.libRoot import getLibRoot

class YamlConfigReaderTest(unittest.TestCase):

    def setUp(self):
        self.__yamlConfigReader = YamlConfigReader()

    def test_basic(self):
        config = self.__yamlConfigReader.read(getLibRoot() + '/config/YamlConfigReaderTest/basic/config.yaml')
        parameters = config['parameters']

        self.assertFalse('imports' in config)
        self.assertEqual(123, parameters['paramLevel1'])
        self.assertEqual(456, parameters['paramLevel2'])
        self.assertEqual(666, parameters['paramLevel3'])
        self.assertEqual(1, parameters['mergedParam']['level1'])
        self.assertEqual(2, parameters['mergedParam']['level2'])
        self.assertEqual(3, parameters['mergedParam']['level3'])
        self.assertEqual(111, parameters['paramToOverwrite'])

    def test_search(self):
        config = self.__yamlConfigReader.read(getLibRoot() + '/config/YamlConfigReaderTest/search/_config/config.yaml')
        parameters = config['parameters']

        self.assertFalse('imports' in config)
        self.assertEqual(123, parameters['paramLevel1'])
        self.assertEqual(456, parameters['paramLevel2'])
        self.assertEqual(789, parameters['paramLevel3'])
        self.assertEqual(1, parameters['mergedParam']['level1'])
        self.assertEqual(2, parameters['mergedParam']['level2'])
        self.assertEqual(3, parameters['mergedParam']['level3'])

if __name__ == '__main__':
    unittest.main()
