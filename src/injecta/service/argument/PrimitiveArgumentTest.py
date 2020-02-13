import unittest

from injecta.service.argument.PrimitiveArgument import PrimitiveArgument

class PrimitiveArgumentTest(unittest.TestCase):

    def test_string(self):
        argument = PrimitiveArgument('ahoj svete')

        self.assertEqual('\'ahoj svete\'', argument.getStringValue())

    def test_number(self):
        argument = PrimitiveArgument(123456)

        self.assertEqual('123456', argument.getStringValue())

    def test_bool(self):
        argument = PrimitiveArgument(True)

        self.assertEqual('True', argument.getStringValue())

    def test_none(self):
        argument = PrimitiveArgument(None)

        self.assertEqual('None', argument.getStringValue())

    def test_envPlaceholderOnly(self):
        argument = PrimitiveArgument('%env(APP_ENV)%')

        self.assertEqual('os.environ[\'APP_ENV\']', argument.getStringValue())

    def test_valuePlaceholderOnly(self):
        argument = PrimitiveArgument('%foo.bar%')

        self.assertEqual('self.__parameters.foo.bar', argument.getStringValue())

    def test_envPlaceholder(self):
        argument = PrimitiveArgument('ahoj %env(APP_ENV)%')

        self.assertEqual('\'ahoj \' + os.environ[\'APP_ENV\']', argument.getStringValue())

    def test_valuePlaceholder(self):
        argument = PrimitiveArgument('ahoj %foo.bar%')

        self.assertEqual('\'ahoj \' + self.__parameters.foo.bar', argument.getStringValue())

    def test_placeholderCombination(self):
        argument = PrimitiveArgument('ahoj %foo.bar% svete %env(APP_ENV)% novy')

        self.assertEqual('\'ahoj \' + self.__parameters.foo.bar + \' svete \' + os.environ[\'APP_ENV\'] + \' novy\'', argument.getStringValue())

    def test_placeholderCombination2(self):
        argument = PrimitiveArgument('%foo.bar% svete %env(APP_ENV)%')

        self.assertEqual('self.__parameters.foo.bar + \' svete \' + os.environ[\'APP_ENV\']', argument.getStringValue())

if __name__ == '__main__':
    unittest.main()
