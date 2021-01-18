import unittest
from injecta.service.argument.ServiceArgument import ServiceArgument
from injecta.dtype.DType import DType
from injecta.service.argument.PrimitiveArgument import PrimitiveArgument
from injecta.service.argument.validator.ArgumentsValidator import ArgumentsValidator
from injecta.service.class_.InspectedArgument import InspectedArgument
from injecta.service.resolved.ResolvedArgument import ResolvedArgument

class ArgumentsValidatorTest(unittest.TestCase):

    def setUp(self):
        self.__argumentsValidator = ArgumentsValidator()

    def test_basic(self):
        self.__argumentsValidator.validate(
            'injecta.mocks.Bar',
            [
                ResolvedArgument(
                    'name',
                    PrimitiveArgument('Jiri Koutny'),
                    InspectedArgument('name', DType('builtins', 'str'))
                )
            ],
            {},
            {},
        )

        self.assertTrue(True)

    def test_exceptionStringForObject(self):
        with self.assertRaises(Exception) as error:
            self.__argumentsValidator.validate(
                'injecta.mocks.Foo',
                [
                    ResolvedArgument(
                        'bar',
                        PrimitiveArgument('Jiri Koutny'),
                        InspectedArgument('bar', DType('injecta.mocks.Bar', 'Bar'))
                    )
                ],
                {},
                {},
            )

        self.assertEqual('Expected dtype "injecta.mocks.Bar.Bar", got "str" (argument "bar", service "injecta.mocks.Foo")', str(error.exception))

    def test_exceptionObjectForString(self):
        with self.assertRaises(Exception) as error:
            self.__argumentsValidator.validate(
                'injecta.mocks.Bar',
                [
                    ResolvedArgument(
                        'name',
                        ServiceArgument('injecta.mocks.Empty'),
                        InspectedArgument('name', DType('builtins', 'str'))
                    )
                ],
                {
                    'injecta.mocks.Empty': DType('injecta.mocks.Empty', 'Empty')
                },
                {},
            )

        self.assertEqual('Expected dtype "str", got "injecta.mocks.Empty.Empty" (argument "name", service "injecta.mocks.Bar")', str(error.exception))

if __name__ == '__main__':
    unittest.main()
