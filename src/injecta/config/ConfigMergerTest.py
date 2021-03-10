import unittest
from injecta.config.ConfigMerger import ConfigMerger


class ConfigMergerTest(unittest.TestCase):
    def setUp(self):
        self.__config_merger = ConfigMerger()

    def test_basic(self):
        a = {
            "hello": {
                "world": 1,
                "street": "Washingtonova",
            },
        }

        b = {
            "hello": {
                "zip": "11000",
            },
        }

        result = self.__config_merger.merge(a, b)

        self.assertEqual(
            {
                "hello": {
                    "world": 1,
                    "street": "Washingtonova",
                    "zip": "11000",
                }
            },
            result,
        )

    def test_overwrite(self):
        a = {
            "hello": {
                "world": 1,
                "street": "Washingtonova",
            },
        }

        b = {
            "hello": {
                "street": "Nova",
                "zip": "11000",
            },
        }

        result = self.__config_merger.merge(a, b)
        expected_result = {
            "hello": {
                "world": 1,
                "street": "Nova",
                "zip": "11000",
            }
        }

        self.assertEqual(expected_result, result)
        # strict dict fields order check
        self.assertEqual(tuple(expected_result["hello"]), tuple(result["hello"]))


if __name__ == "__main__":
    unittest.main()
