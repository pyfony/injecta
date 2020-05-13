import unittest
from injecta.autowiring.ArgumentResolver import ArgumentResolver
from injecta.autowiring.ArgumentsAutowirer import ArgumentsAutowirer
from injecta.dtype.DType import DType
from injecta.service.argument.PrimitiveArgument import PrimitiveArgument
from injecta.service.argument.ServiceArgument import ServiceArgument
from injecta.service.class_.InspectedArgument import InspectedArgument
from injecta.service.resolved.ResolvedArgument import ResolvedArgument

class ArgumentsAutowirerTest(unittest.TestCase):

    def setUp(self):
        self.__argumentsAutowirer = ArgumentsAutowirer(ArgumentResolver())

    def test_basic(self):
        resolvedArguments = [
            ResolvedArgument(
                'myNumber',
                PrimitiveArgument(123),
                InspectedArgument('myNumber', DType('builtins', 'int'))
            ),
            ResolvedArgument(
                'manuallyWiredService',
                ServiceArgument('my.module.ManuallyWiredClass'),
                InspectedArgument('manuallyWiredService', DType('my.module.ManuallyWiredClass', 'ManuallyWiredClass'))
            ),
            ResolvedArgument(
                'autowiredService',
                None,
                InspectedArgument('autowiredService', DType('my.module.OtherClass', 'OtherClass')),
            )
        ]

        classes2Services = {
            'my.module.OtherClass': {'OtherClass': ['my.module.OtherClass']}
        }

        newResolvedArguments = self.__argumentsAutowirer.autowire(
            'my.module.MyClass',
            resolvedArguments,
            classes2Services,
        )

        self.assertEqual(3, len(newResolvedArguments))
        self.assertEqual(PrimitiveArgument(123), newResolvedArguments[0].argument)
        self.assertEqual(ServiceArgument('my.module.ManuallyWiredClass'), newResolvedArguments[1].argument)
        self.assertEqual(ServiceArgument('my.module.OtherClass', 'autowiredService'), newResolvedArguments[2].argument)

    def test_namedArguments(self):
        resolvedArguments = [
            ResolvedArgument(
                'myNumber',
                PrimitiveArgument(123, 'myNumber'),
                InspectedArgument('myNumber', DType('builtins', 'int'))
            ),
            ResolvedArgument(
                'manuallyWiredService',
                ServiceArgument('my.module.ManuallyWiredClass', 'manuallyWiredService'),
                InspectedArgument('manuallyWiredService', DType('my.module.ManuallyWiredClass', 'ManuallyWiredClass'))
            ),
            ResolvedArgument(
                'autowiredService',
                None,
                InspectedArgument('autowiredService', DType('my.module.OtherClass', 'OtherClass')),
            )
        ]

        classes2Services = {
            'my.module.OtherClass': {'OtherClass': ['my.module.OtherClass']}
        }

        newResolvedArguments = self.__argumentsAutowirer.autowire(
            'my.module.MyClass',
            resolvedArguments,
            classes2Services,
        )

        self.assertEqual(3, len(newResolvedArguments))
        self.assertEqual(PrimitiveArgument(123, 'myNumber'), newResolvedArguments[0].argument)
        self.assertEqual(ServiceArgument('my.module.ManuallyWiredClass', 'manuallyWiredService'), newResolvedArguments[1].argument)
        self.assertEqual(ServiceArgument('my.module.OtherClass', 'autowiredService'), newResolvedArguments[2].argument)

if __name__ == '__main__':
    unittest.main()
