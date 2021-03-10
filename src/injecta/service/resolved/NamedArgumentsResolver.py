from typing import List, Dict
from injecta.service.argument.ArgumentInterface import ArgumentInterface
from injecta.service.class_.InspectedArgument import InspectedArgument
from injecta.service.resolved.ResolvedArgument import ResolvedArgument
from injecta.service.argument.validator.ArgumentsValidator import ArgumentsValidator
from injecta.service.class_.InspectedArgumentsResolver import InspectedArgumentsResolver


class NamedArgumentsResolver:
    def __init__(self):
        self.__inspected_arguments_resolver = InspectedArgumentsResolver()
        self.__arguments_validator = ArgumentsValidator()

    def resolve(self, arguments: List[ArgumentInterface], inspected_arguments: List[InspectedArgument], service_name: str):
        inspected_arguments = [inspected_argument for inspected_argument in inspected_arguments if inspected_argument.name != "args"]
        inspected_arguments_indexed = {inspected_argument.name: inspected_argument for inspected_argument in inspected_arguments}
        arguments_indexed = {argument.name: argument for argument in arguments}

        if self.__contains_kwargs(inspected_arguments):
            return self.__resolve_arguments_kwargs(arguments_indexed, inspected_arguments_indexed)

        for argument_name, argument in arguments_indexed.items():
            if argument_name not in inspected_arguments_indexed:
                raise Exception(f'Unknown argument "{argument_name}" in service "{service_name}"')

        return self.__resolve_arguments(arguments_indexed, inspected_arguments_indexed)

    def __resolve_arguments_kwargs(
        self, arguments_indexed: Dict[str, ArgumentInterface], inspected_arguments_indexed: Dict[str, InspectedArgument]
    ):
        del inspected_arguments_indexed["kwargs"]
        resolved_arguments = self.__resolve_arguments(arguments_indexed, inspected_arguments_indexed)

        for resolved_argument in resolved_arguments:
            del arguments_indexed[resolved_argument.name]

        for _, argument in arguments_indexed.items():
            resolved_arguments.append(ResolvedArgument(argument.name, argument, None))

        return resolved_arguments

    def __resolve_arguments(
        self, arguments_indexed: Dict[str, ArgumentInterface], inspected_arguments_indexed: Dict[str, InspectedArgument]
    ):
        resolved_arguments = []

        for argument_name, inspected_argument in inspected_arguments_indexed.items():
            argument = arguments_indexed[argument_name] if argument_name in arguments_indexed else None

            # argument with default value, no value defined in service configuration
            if inspected_argument.has_default_value() and argument is None:
                continue

            resolved_argument = ResolvedArgument(inspected_argument.name, argument, inspected_argument)

            resolved_arguments.append(resolved_argument)

        return resolved_arguments

    def __contains_kwargs(self, inspected_arguments: List[InspectedArgument]):
        return inspected_arguments and inspected_arguments[-1].name == "kwargs"
