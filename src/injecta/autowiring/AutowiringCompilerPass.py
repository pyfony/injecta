from injecta.autowiring.ArgumentsAutowirer import ArgumentsAutowirer
from injecta.compiler.CompilerPassInterface import CompilerPassInterface
from injecta.container.ContainerBuild import ContainerBuild
from injecta.service.resolved.ResolvedService import ResolvedService

class AutowiringCompilerPass(CompilerPassInterface):

    def __init__(self, argumentsAutowirer: ArgumentsAutowirer):
        self.__argumentsAutowirer = argumentsAutowirer

    def process(self, containerBuild: ContainerBuild):
        def shouldAutowire(resolvedService: ResolvedService):
            return resolvedService.service.autowire is True and resolvedService.resolvedArguments

        servicesForAutowiring = list(filter(shouldAutowire, containerBuild.resolvedServices))

        for resolvedService in servicesForAutowiring:
            self.__autowire(resolvedService, containerBuild.classes2Services)

    def __autowire(self, resolvedService: ResolvedService, classes2Services: dict):
        resolvedArguments = self.__argumentsAutowirer.autowire(
            resolvedService.service.name,
            resolvedService.resolvedArguments,
            classes2Services,
        )

        resolvedService.replaceResolvedArguments(resolvedArguments)
