from typing import List
from injecta.service.argument.ArgumentInterface import ArgumentInterface
from injecta.service.class_.InspectedArgument import InspectedArgument
from injecta.service.resolved.ResolvedArgument import ResolvedArgument
from injecta.service.argument.validator.ArgumentsValidator import ArgumentsValidator
from injecta.service.class_.InspectedArgumentsResolver import InspectedArgumentsResolver

class ArgumentListResolver:

    def __init__(self):
        self.__inspectedArgumentsResolver = InspectedArgumentsResolver()
        self.__argumentsValidator = ArgumentsValidator()

    def resolve(self, arguments: List[ArgumentInterface], inspectedArguments: List[InspectedArgument], serviceName: str):
        if self.__containsKwargs(inspectedArguments):
            raise Exception(f'__init__() in service "{serviceName}" contains **kwargs, use named arguments instead')

        containsArgs = self.__containsArgs(inspectedArguments)

        if not containsArgs and len(arguments) > len(inspectedArguments):
            raise Exception(f'Too many arguments given for "{serviceName}"')

        if containsArgs:
            return self.__resolveArgumentsArgs(arguments, inspectedArguments)

        return self.__resolveArguments(arguments, inspectedArguments)

    def __resolveArgumentsArgs(self, arguments: List[ArgumentInterface], inspectedArguments: List[InspectedArgument]):
        resolvedArguments = self.__resolveArguments(arguments, inspectedArguments[0:-1])

        startIndex = len(resolvedArguments)

        for idx, argument in enumerate(arguments[startIndex:]):
            resolvedArguments.append(ResolvedArgument(f'arg_{idx}', argument, None))

        return resolvedArguments

    def __resolveArguments(self, arguments: List[ArgumentInterface], inspectedArguments: List[InspectedArgument]):
        resolvedArguments = []
        argumentCount = len(arguments)

        for idx, inspectedArgument in enumerate(inspectedArguments):
            argument = arguments[idx] if idx < argumentCount else None

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

    def __containsArgs(self, inspectedArguments: List[InspectedArgument]):
        return inspectedArguments and inspectedArguments[-1].name == 'args'

    def __containsKwargs(self, inspectedArguments: List[InspectedArgument]):
        return inspectedArguments and inspectedArguments[-1].name == 'kwargs'
