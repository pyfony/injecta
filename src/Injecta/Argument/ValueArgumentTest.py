import unittest

from Injecta.Argument.ValueArgument import ValueArgument

class ValueArgumentTest(unittest.TestCase):

    def test_string(self):
        valueArgument = ValueArgument('ahoj svete')

        self.assertEqual('\'ahoj svete\'', valueArgument.getValue())

    def test_number(self):
        valueArgument = ValueArgument(123456)

        self.assertEqual(123456, valueArgument.getValue())

    def test_bool(self):
        valueArgument = ValueArgument(True)

        self.assertEqual('True', valueArgument.getValue())

    def test_envPlaceholderOnly(self):
        valueArgument = ValueArgument('%env(APP_ENV)%')

        self.assertEqual('os.environ[\'APP_ENV\']', valueArgument.getValue())

    def test_valuePlaceholderOnly(self):
        valueArgument = ValueArgument('%foo.bar%')

        self.assertEqual('self.__parameters.foo.bar', valueArgument.getValue())

    def test_envPlaceholder(self):
        valueArgument = ValueArgument('ahoj %env(APP_ENV)%')

        self.assertEqual('\'ahoj \' + os.environ[\'APP_ENV\']', valueArgument.getValue())

    def test_valuePlaceholder(self):
        valueArgument = ValueArgument('ahoj %foo.bar%')

        self.assertEqual('\'ahoj \' + self.__parameters.foo.bar', valueArgument.getValue())

    def test_placeholderCombination(self):
        valueArgument = ValueArgument('ahoj %foo.bar% svete %env(APP_ENV)% novy')

        self.assertEqual('\'ahoj \' + self.__parameters.foo.bar + \' svete \' + os.environ[\'APP_ENV\'] + \' novy\'', valueArgument.getValue())

    def test_placeholderCombination2(self):
        valueArgument = ValueArgument('%foo.bar% svete %env(APP_ENV)%')

        self.assertEqual('self.__parameters.foo.bar + \' svete \' + os.environ[\'APP_ENV\']', valueArgument.getValue())

if __name__ == '__main__':
    unittest.main()
