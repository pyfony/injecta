from typing import List
from injecta.autowiring.ArgumentResolver import ArgumentResolver
from injecta.container.ContainerInterface import ContainerInterface
from injecta.service.argument.ServiceArgument import ServiceArgument
from injecta.service.resolved.ResolvedArgument import ResolvedArgument

class ArgumentsAutowirer:

    def __init__(self, argumentResolver: ArgumentResolver):
        self.__argumentResolver = argumentResolver

    def autowire(self, serviceName: str, resolvedArguments: List[ResolvedArgument], classes2Services: dict):
        def autowireArgument(resolvedArgument: ResolvedArgument):
            if resolvedArgument.argument or resolvedArgument.inspectedArgument.hasDefaultValue():
                return resolvedArgument

            if resolvedArgument.inspectedArgument.dtype.moduleName == ContainerInterface.__module__:
                serviceArgument = ServiceArgument('serviceContainer', resolvedArgument.name)
                resolvedArgument.modifyArgument(serviceArgument, 'container autowiring')

                return resolvedArgument

            serviceArgument = self.__argumentResolver.resolve(resolvedArgument.inspectedArgument, serviceName, classes2Services)
            resolvedArgument.modifyArgument(serviceArgument, 'autowiring')

            return resolvedArgument

        return list(map(autowireArgument, resolvedArguments))
