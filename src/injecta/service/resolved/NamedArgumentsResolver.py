from typing import List, Dict
from injecta.service.argument.ArgumentInterface import ArgumentInterface
from injecta.service.class_.InspectedArgument import InspectedArgument
from injecta.service.resolved.ResolvedArgument import ResolvedArgument
from injecta.service.ServiceValidator import ServiceValidator
from injecta.service.class_.InspectedArgumentsResolver import InspectedArgumentsResolver

class NamedArgumentsResolver:

    def __init__(self):
        self.__inspectedArgumentsResolver = InspectedArgumentsResolver()
        self.__serviceValidator = ServiceValidator()

    def resolve(self, arguments: List[ArgumentInterface], inspectedArguments: List[InspectedArgument], serviceName: str):
        inspectedArgumentsIndexed = {inspectedArgument.name: inspectedArgument for inspectedArgument in inspectedArguments}
        argumentsIndexed = {argument.name: argument for argument in arguments}

        if self.__containsKwargs(inspectedArguments):
            return self.__resolveArgumentsKwargs(argumentsIndexed, inspectedArgumentsIndexed)

        for argumentName, argument in argumentsIndexed.items():
            if argumentName not in inspectedArgumentsIndexed:
                raise Exception(f'Unknown argument "{argumentName}" in service "{serviceName}"')

        return self.__resolveArguments(argumentsIndexed, inspectedArgumentsIndexed)

    def __resolveArgumentsKwargs(self, argumentsIndexed: Dict[str, ArgumentInterface], inspectedArgumentsIndexed: Dict[str, InspectedArgument]):
        del inspectedArgumentsIndexed['kwargs']
        resolvedArguments = self.__resolveArguments(argumentsIndexed, inspectedArgumentsIndexed)

        for resolvedArgument in resolvedArguments:
            del argumentsIndexed[resolvedArgument.name]

        for _, argument in argumentsIndexed.items():
            resolvedArguments.append(ResolvedArgument(argument.name, argument, None))

        return resolvedArguments

    def __resolveArguments(self, argumentsIndexed: Dict[str, ArgumentInterface], inspectedArgumentsIndexed: Dict[str, InspectedArgument]):
        resolvedArguments = []

        for argumentName, inspectedArgument in inspectedArgumentsIndexed.items():
            argument = argumentsIndexed[argumentName] if argumentName in argumentsIndexed else None

            # argument with default value, no value defined in service configuration
            if inspectedArgument.hasDefaultValue() and argument is None:
                continue

            resolvedArgument = ResolvedArgument(
                inspectedArgument.name,
                argument,
                inspectedArgument
            )

            resolvedArguments.append(resolvedArgument)

        return resolvedArguments

    def __containsKwargs(self, inspectedArguments: List[InspectedArgument]):
        return inspectedArguments and inspectedArguments[-1].name == 'kwargs'
