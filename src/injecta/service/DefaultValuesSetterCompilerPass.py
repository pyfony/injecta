from injecta.compiler.CompilerPassInterface import CompilerPassInterface
from injecta.container.ContainerBuild import ContainerBuild
from injecta.service.DefaultValuesSetter import DefaultValuesSetter
from injecta.service.resolved.ResolvedService import ResolvedService

class DefaultValuesSetterCompilerPass(CompilerPassInterface):

    def __init__(self, defaultValuesSetter: DefaultValuesSetter):
        self.__defaultValuesSetter = defaultValuesSetter

    def process(self, containerBuild: ContainerBuild):
        for resolvedService in containerBuild.resolvedServices:
            self.__setDefaultValues(resolvedService)

    def __setDefaultValues(self, resolvedService: ResolvedService):
        service = resolvedService.service

        if service.usesFactory():
            return

        newArguments = self.__defaultValuesSetter.set(
            service.arguments,
            resolvedService.constructorArguments,
        )

        service.setArguments(newArguments)
