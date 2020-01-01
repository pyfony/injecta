import unittest

from injecta.definition.argument.ServiceArgument import ServiceArgument
from injecta.dtype.DType import DType
from injecta.definition.argument.PrimitiveArgument import PrimitiveArgument
from injecta.service.ServiceValidator import ServiceValidator
from injecta.service.class_.ConstructorArgumentsResolver import ConstructorArgumentsResolver

class ServiceValidatorTest(unittest.TestCase):

    def setUp(self):
        self.__serviceValidator = ServiceValidator()
        self.__constructorArgumentsResolver = ConstructorArgumentsResolver()

    def test_basic(self):
        self.__serviceValidator.validate(
            'injecta.mocks.Bar',
            [
                PrimitiveArgument('Jiri Koutny'),
            ],
            self.__constructorArgumentsResolver.resolve(DType('injecta.mocks.Bar', 'Bar')),
            {},
        )

        self.assertTrue(True)

    def test_moreArgumentsDefinedException(self):
        try:
            self.__serviceValidator.validate(
                'injecta.mocks.Bar',
                [
                    PrimitiveArgument('Jiri Koutny'),
                ],
                [],
                {},
            )

            self.fail('Exception must be thrown')
        except Exception as e:
            self.assertEqual('More arguments defined than given for "injecta.mocks.Bar"', str(e))

    def test_exceptionStringForObject(self):
        try:
            self.__serviceValidator.validate(
                'injecta.mocks.Foo',
                [
                    PrimitiveArgument('Jiri Koutny'),
                ],
                self.__constructorArgumentsResolver.resolve(DType('injecta.mocks.Foo', 'Foo')),
                {},
            )

            self.fail('Exception must be thrown')
        except Exception as e:
            self.assertEqual('Expected dtype "injecta.mocks.Bar.Bar", got "str" (argument "bar", service "injecta.mocks.Foo")', str(e))

    def test_exceptionObjectForString(self):
        try:
            self.__serviceValidator.validate(
                'injecta.mocks.Bar',
                [
                    ServiceArgument('injecta.mocks.Empty'),
                ],
                self.__constructorArgumentsResolver.resolve(DType('injecta.mocks.Bar', 'Bar')),
                {
                    'injecta.mocks.Empty': DType('injecta.mocks.Empty', 'Empty')
                },
            )

            self.fail('Exception must be thrown')
        except Exception as e:
            self.assertEqual('Expected dtype "str", got "injecta.mocks.Empty.Empty" (argument "name", service "injecta.mocks.Bar")', str(e))

if __name__ == '__main__':
    unittest.main()
