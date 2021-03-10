import unittest
from injecta.parameter.placeholder_replacer import replace_placeholder


class placeholder_replacer_test(unittest.TestCase):  # noqa: N801
    def test_string(self):
        result = replace_placeholder("hello %name%", "name", "Jiri", "company.owner")

        self.assertEqual("hello Jiri", result)

    def test_int_solo(self):
        result = replace_placeholder("%house_number%", "house_number", 3901, "company.address")

        self.assertEqual(3901, result)

    def test_int_concat(self):
        result = replace_placeholder("House number: %house_number%", "house_number", 3901, "company.address")

        self.assertEqual("House number: 3901", result)

    def test_list_solo(self):
        result = replace_placeholder("%emails%", "emails", ["me@me.com", "johny@example.com"], "job.on_error_notifications")

        self.assertEqual(["me@me.com", "johny@example.com"], result)

    def test_list_concat(self):
        with self.assertRaises(Exception) as error:
            replace_placeholder("Emails: %emails%", "emails", ["me@me.com", "johny@example.com"], "job.on_error_notifications")

        self.assertEqual(
            "Merging list parameters with other variable types is not allowed in job.on_error_notifications", str(error.exception)
        )

    def test_none_solo(self):
        result = replace_placeholder("%instance_type%", "instance_type", None, "job.cluster_instance")

        self.assertEqual(None, result)

    def test_none_concat(self):
        with self.assertRaises(Exception) as error:
            replace_placeholder("Instance type: %instance_type%", "instance_type", None, "job.cluster_instance")

        self.assertEqual("Merging None value with other variable types is not allowed in job.cluster_instance", str(error.exception))


if __name__ == "__main__":
    unittest.main()
