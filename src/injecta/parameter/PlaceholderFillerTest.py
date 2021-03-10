import unittest
from injecta.parameter.PlaceholderFiller import PlaceholderFiller
import os


class PlaceholderFillerTest(unittest.TestCase):
    def setUp(self):
        self.__placeholder_filler = PlaceholderFiller()

    def test_basic_multi_level(self):
        result = self.__placeholder_filler.fill(
            {
                "level_1": "1",
                "level_2_1": "2 + %level_1%",
                "level_3_2_1": "3 + %level_2_1%",
                "level_4_3_2_1": "4 + %level_3_2_1%",
            }
        )

        self.assertEqual("1", result["level_1"])
        self.assertEqual("2 + 1", result["level_2_1"])
        self.assertEqual("3 + 2 + 1", result["level_3_2_1"])
        self.assertEqual("4 + 3 + 2 + 1", result["level_4_3_2_1"])

    def test_multiple_placeholders(self):
        result = self.__placeholder_filler.fill(
            {
                "level_1": "1",
                "level_2_1": "2 + %level_1%",
                "level_3": "3",
                "level_4_3_2_1": "4 + %level_3% + %level_2_1%",
            }
        )

        self.assertEqual("1", result["level_1"])
        self.assertEqual("2 + 1", result["level_2_1"])
        self.assertEqual("4 + 3 + 2 + 1", result["level_4_3_2_1"])

    def test_types_consistency(self):
        result = self.__placeholder_filler.fill(
            {
                "typed_values": {
                    "number": 123456,
                    "bool": True,
                    "none": None,
                },
                "referenced_typed_values": {
                    "number": "%typed_values.number%",
                    "bool": "%typed_values.bool%",
                    "none": "%typed_values.none%",
                },
            }
        )

        self.assertEqual(123456, result["referenced_typed_values"]["number"])
        self.assertEqual(True, result["referenced_typed_values"]["bool"])
        self.assertEqual(None, result["referenced_typed_values"]["none"])

    def test_env_variables(self):
        os.environ["LEVEL_1"] = "1"

        result = self.__placeholder_filler.fill(
            {
                "level_2_1": "2 + %env(LEVEL_1)%",
                "level_3_2_1": "3 + %level_2_1%",
                "level_4_3_2_1": "4 + %level_3_2_1%",
            }
        )

        self.assertEqual("2 + 1", result["level_2_1"])
        self.assertEqual("3 + 2 + 1", result["level_3_2_1"])
        self.assertEqual("4 + 3 + 2 + 1", result["level_4_3_2_1"])

    def test_full(self):
        os.environ["APP_ENV"] = "dev"

        result = self.__placeholder_filler.fill(
            {
                "first": {
                    "second": {
                        "third": 52,
                    }
                },
                "my_list": ["/foo/bar", "%project_root%/ahoj/svete/%first.second.third%", "%project.root_path%/ahoj/svete"],
                "paths": {
                    "parties_path": "/foo/bar",
                    "orders_path": "%project_root%/ahoj/svete/%first.second.third%",
                    "projects_path": "%project.root_path%/ahoj/svete",
                },
                "project_root": "/%env(APP_ENV)%/myroot",
                "project": {
                    "root_path": "/project_root_path",
                },
                "my_list_linked": "%my_list%",
                "my_dict_linked": "%paths%",
            }
        )

        self.assertEqual("/dev/myroot/ahoj/svete/52", result["paths"]["orders_path"])
        self.assertEqual("/project_root_path/ahoj/svete", result["paths"]["projects_path"])
        self.assertEqual("/foo/bar", result["my_list"][0])
        self.assertEqual("/dev/myroot/ahoj/svete/52", result["my_list"][1])
        self.assertEqual("/dev/myroot/ahoj/svete/52", result["my_list_linked"][1])
        self.assertEqual("/project_root_path/ahoj/svete", result["my_dict_linked"]["projects_path"])

    def test_non_existing(self):
        with self.assertRaises(Exception) as cm:
            self.__placeholder_filler.fill(
                {
                    "first": {"second": {"third": "52"}},
                    "paths": {
                        "orders_path": "ahoj/%first.second.thirdddddd%",
                    },
                }
            )

        self.assertEqual('Parameter "first.second.thirdddddd" used in paths.orders_path not found', str(cm.exception))

    def test_non_existing_env_var(self):
        with self.assertRaises(Exception) as cm:
            self.__placeholder_filler.fill({"first": {"second": "%env(NON_EXISTENT_ENV_VAR)%"}})

        self.assertEqual('Undefined environment variable "NON_EXISTENT_ENV_VAR" used in first.second', str(cm.exception))


if __name__ == "__main__":
    unittest.main()
