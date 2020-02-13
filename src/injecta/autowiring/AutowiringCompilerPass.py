from injecta.autowiring.ArgumentsAutowirer import ArgumentsAutowirer
from injecta.compiler.CompilerPassInterface import CompilerPassInterface
from injecta.container.ContainerBuild import ContainerBuild
from injecta.service.resolved.ResolvedService import ResolvedService

class AutowiringCompilerPass(CompilerPassInterface):

    def __init__(self, argumentsAutowirer: ArgumentsAutowirer):
        self.__argumentsAutowirer = argumentsAutowirer

    def process(self, containerBuild: ContainerBuild):
        def shouldAutowire(resolvedService: ResolvedService):
            return resolvedService.service.autowire is True and resolvedService.constructorArguments

        servicesForAutowiring = list(filter(shouldAutowire, containerBuild.resolvedServices))

        for service in servicesForAutowiring:
            self.__autowire(service, containerBuild.classes2Services)

    def __autowire(self, resolvedService: ResolvedService, classes2Services: dict):
        service = resolvedService.service

        newArguments = self.__argumentsAutowirer.autowire(
            service.name,
            service.arguments,
            resolvedService.constructorArguments,
            classes2Services,
        )

        service.setArguments(newArguments)
