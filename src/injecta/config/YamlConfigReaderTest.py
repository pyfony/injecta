import unittest
from injecta.config.YamlConfigReader import YamlConfigReader
from injecta.lib_root import get_lib_root


class YamlConfigReaderTest(unittest.TestCase):
    def setUp(self):
        self.__yaml_config_reader = YamlConfigReader()

    def test_basic(self):
        config = self.__yaml_config_reader.read(get_lib_root() + "/config/YamlConfigReaderTest/basic/config.yaml")
        parameters = config["parameters"]

        self.assertFalse("imports" in config)
        self.assertEqual(123, parameters["param_level1"])
        self.assertEqual(456, parameters["param_level2"])
        self.assertEqual(666, parameters["param_level3"])
        self.assertEqual(1, parameters["merged_param"]["level1"])
        self.assertEqual(2, parameters["merged_param"]["level2"])
        self.assertEqual(3, parameters["merged_param"]["level3"])
        self.assertEqual(111, parameters["param_to_overwrite"])

    def test_search(self):
        config = self.__yaml_config_reader.read(get_lib_root() + "/config/YamlConfigReaderTest/search/_config/config.yaml")
        parameters = config["parameters"]

        self.assertFalse("imports" in config)
        self.assertEqual(123, parameters["param_level1"])
        self.assertEqual(456, parameters["param_level2"])
        self.assertEqual(789, parameters["param_level3"])
        self.assertEqual(1, parameters["merged_param"]["level1"])
        self.assertEqual(2, parameters["merged_param"]["level2"])
        self.assertEqual(3, parameters["merged_param"]["level3"])


if __name__ == "__main__":
    unittest.main()
