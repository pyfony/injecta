from typing import List
from injecta.definition.argument.ArgumentInterface import ArgumentInterface
from injecta.autowiring.ArgumentResolver import ArgumentResolver
from injecta.service.class_.ConstructorArgument import ConstructorArgument

class ArgumentsAutowirer:

    def __init__(self, argumentResolver: ArgumentResolver):
        self.__argumentResolver = argumentResolver

    def autowire(self, serviceName: str, arguments: List[ArgumentInterface], constructorArguments: List[ConstructorArgument], classes2Services: dict):
        newArguments = []

        i = 1
        for constructorArgument in constructorArguments:
            if i <= len(arguments):
                newArgument = arguments[i - 1]
            else:
                newArgument = self.__argumentResolver.resolve(constructorArgument, serviceName, classes2Services)

            newArguments.append(newArgument)

            i += 1

        return newArguments
