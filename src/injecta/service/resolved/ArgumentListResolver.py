from typing import List
from injecta.service.argument.ArgumentInterface import ArgumentInterface
from injecta.service.class_.InspectedArgument import InspectedArgument
from injecta.service.resolved.ResolvedArgument import ResolvedArgument
from injecta.service.argument.validator.ArgumentsValidator import ArgumentsValidator
from injecta.service.class_.InspectedArgumentsResolver import InspectedArgumentsResolver


class ArgumentListResolver:
    def __init__(self):
        self.__inspected_arguments_resolver = InspectedArgumentsResolver()
        self.__arguments_validator = ArgumentsValidator()

    def resolve(self, arguments: List[ArgumentInterface], inspected_arguments: List[InspectedArgument], service_name: str):
        if self.__contains_kwargs(inspected_arguments):
            raise Exception(f'__init__() in service "{service_name}" contains **kwargs, use named arguments instead')

        contains_args = self.__contains_args(inspected_arguments)

        if not contains_args and len(arguments) > len(inspected_arguments):
            raise Exception(f'Too many arguments given for service "{service_name}"')

        if contains_args:
            return self.__resolve_arguments_args(arguments, inspected_arguments)

        return self.__resolve_arguments(arguments, inspected_arguments)

    def __resolve_arguments_args(self, arguments: List[ArgumentInterface], inspected_arguments: List[InspectedArgument]):
        resolved_arguments = self.__resolve_arguments(arguments, inspected_arguments[0:-1])

        start_index = len(resolved_arguments)

        for idx, argument in enumerate(arguments[start_index:]):
            resolved_arguments.append(ResolvedArgument(f"arg_{idx}", argument, None))

        return resolved_arguments

    def __resolve_arguments(self, arguments: List[ArgumentInterface], inspected_arguments: List[InspectedArgument]):
        resolved_arguments = []
        argument_count = len(arguments)

        for idx, inspected_argument in enumerate(inspected_arguments):
            argument = arguments[idx] if idx < argument_count else None

            # argument with default value, no value defined in service configuration
            if inspected_argument.has_default_value() and argument is None:
                continue

            resolved_argument = ResolvedArgument(inspected_argument.name, argument, inspected_argument)

            resolved_arguments.append(resolved_argument)

        return resolved_arguments

    def __contains_args(self, inspected_arguments: List[InspectedArgument]):
        return inspected_arguments and inspected_arguments[-1].name == "args"

    def __contains_kwargs(self, inspected_arguments: List[InspectedArgument]):
        return inspected_arguments and inspected_arguments[-1].name == "kwargs"
