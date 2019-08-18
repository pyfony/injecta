import unittest
from Injecta.Config.YamlConfigReader import YamlConfigReader
from Injecta.LibRoot import getLibRoot

class YamlConfigReaderTest(unittest.TestCase):

    def setUp(self):
        self.__yamlConfigReader = YamlConfigReader()

    def test_basic(self):
        config = self.__yamlConfigReader.read(getLibRoot() + '/Config/YamlConfigReaderTest/basic/config.yaml')
        parameters = config['parameters']

        self.assertFalse('imports' in config)
        self.assertEqual(123, parameters['paramLevel1'])
        self.assertEqual(456, parameters['paramLevel2'])
        self.assertEqual(789, parameters['paramLevel3'])
        self.assertEqual(1, parameters['mergedParam']['level1'])
        self.assertEqual(2, parameters['mergedParam']['level2'])
        self.assertEqual(3, parameters['mergedParam']['level3'])

    def test_search(self):
        config = self.__yamlConfigReader.read(getLibRoot() + '/Config/YamlConfigReaderTest/search/_config/config.yaml')
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
