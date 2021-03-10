import unittest

from injecta.service.argument.PrimitiveArgument import PrimitiveArgument


class PrimitiveArgumentTest(unittest.TestCase):
    def test_string(self):
        argument = PrimitiveArgument("hello world")

        self.assertEqual("'hello world'", argument.get_string_value())

    def test_number(self):
        argument = PrimitiveArgument(123456)

        self.assertEqual("123456", argument.get_string_value())

    def test_bool(self):
        argument = PrimitiveArgument(True)

        self.assertEqual("True", argument.get_string_value())

    def test_none(self):
        argument = PrimitiveArgument(None)

        self.assertEqual("None", argument.get_string_value())

    def test_env_placeholder_only(self):
        argument = PrimitiveArgument("%env(APP_ENV)%")

        self.assertEqual("os.environ['APP_ENV']", argument.get_string_value())

    def test_value_placeholder_only(self):
        argument = PrimitiveArgument("%foo.bar%")

        self.assertEqual("self.__parameters.foo.bar", argument.get_string_value())

    def test_env_placeholder(self):
        argument = PrimitiveArgument("ahoj %env(APP_ENV)%")

        self.assertEqual("'ahoj ' + os.environ['APP_ENV']", argument.get_string_value())

    def test_value_placeholder(self):
        argument = PrimitiveArgument("ahoj %foo.bar%")

        self.assertEqual("'ahoj ' + self.__parameters.foo.bar", argument.get_string_value())

    def test_placeholder_combination(self):
        argument = PrimitiveArgument("ahoj %foo.bar% svete %env(APP_ENV)% novy")

        self.assertEqual("'ahoj ' + self.__parameters.foo.bar + ' svete ' + os.environ['APP_ENV'] + ' novy'", argument.get_string_value())

    def test_placeholder_combination2(self):
        argument = PrimitiveArgument("%foo.bar% svete %env(APP_ENV)%")

        self.assertEqual("self.__parameters.foo.bar + ' svete ' + os.environ['APP_ENV']", argument.get_string_value())


if __name__ == "__main__":
    unittest.main()
