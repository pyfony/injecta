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
        self.__arguments_autowirer = ArgumentsAutowirer(ArgumentResolver())

    def test_basic(self):
        resolved_arguments = [
            ResolvedArgument("my_number", PrimitiveArgument(123), InspectedArgument("my_number", DType("builtins", "int"))),
            ResolvedArgument(
                "manually_wired_service",
                ServiceArgument("my.module.ManuallyWiredClass"),
                InspectedArgument("manually_wired_service", DType("my.module.ManuallyWiredClass", "ManuallyWiredClass")),
            ),
            ResolvedArgument(
                "autowired_service",
                None,
                InspectedArgument("autowired_service", DType("my.module.OtherClass", "OtherClass")),
            ),
        ]

        classes2_services = {"my.module.OtherClass": {"OtherClass": ["my.module.OtherClass"]}}

        new_resolved_arguments = self.__arguments_autowirer.autowire(
            "my.module.MyClass",
            resolved_arguments,
            classes2_services,
        )

        self.assertEqual(3, len(new_resolved_arguments))
        self.assertEqual(PrimitiveArgument(123), new_resolved_arguments[0].argument)
        self.assertEqual(ServiceArgument("my.module.ManuallyWiredClass"), new_resolved_arguments[1].argument)
        self.assertEqual(ServiceArgument("my.module.OtherClass", "autowired_service"), new_resolved_arguments[2].argument)

    def test_named_arguments(self):
        resolved_arguments = [
            ResolvedArgument("my_number", PrimitiveArgument(123, "my_number"), InspectedArgument("my_number", DType("builtins", "int"))),
            ResolvedArgument(
                "manually_wired_service",
                ServiceArgument("my.module.ManuallyWiredClass", "manually_wired_service"),
                InspectedArgument("manually_wired_service", DType("my.module.ManuallyWiredClass", "ManuallyWiredClass")),
            ),
            ResolvedArgument(
                "autowired_service",
                None,
                InspectedArgument("autowired_service", DType("my.module.OtherClass", "OtherClass")),
            ),
        ]

        classes2_services = {"my.module.OtherClass": {"OtherClass": ["my.module.OtherClass"]}}

        new_resolved_arguments = self.__arguments_autowirer.autowire(
            "my.module.MyClass",
            resolved_arguments,
            classes2_services,
        )

        self.assertEqual(3, len(new_resolved_arguments))
        self.assertEqual(PrimitiveArgument(123, "my_number"), new_resolved_arguments[0].argument)
        self.assertEqual(ServiceArgument("my.module.ManuallyWiredClass", "manually_wired_service"), new_resolved_arguments[1].argument)
        self.assertEqual(ServiceArgument("my.module.OtherClass", "autowired_service"), new_resolved_arguments[2].argument)


if __name__ == "__main__":
    unittest.main()
