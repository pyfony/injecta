from typing import List
from injecta.autowiring.ArgumentResolver import ArgumentResolver
from injecta.service.resolved.ResolvedArgument import ResolvedArgument

class ArgumentsAutowirer:

    def __init__(self, argumentResolver: ArgumentResolver):
        self.__argumentResolver = argumentResolver

    def autowire(self, serviceName: str, resolvedArguments: List[ResolvedArgument], classes2Services: dict):
        def autowireArgument(resolvedArgument: ResolvedArgument):
            if resolvedArgument.argument or resolvedArgument.inspectedArgument.hasDefaultValue():
                return resolvedArgument

            serviceArgument = self.__argumentResolver.resolve(resolvedArgument.inspectedArgument, serviceName, classes2Services)
            resolvedArgument.modifyArgument(serviceArgument, 'autowiring')

            return resolvedArgument

        return list(map(autowireArgument, resolvedArguments))
