from injecta.compiler.CompilerPassInterface import CompilerPassInterface
from injecta.container.ContainerBuild import ContainerBuild
from injecta.definition.DefaultValuesSetter import DefaultValuesSetter
from injecta.service.Service import Service

class DefaultValuesSetterCompilerPass(CompilerPassInterface):

    def __init__(self, defaultValuesSetter: DefaultValuesSetter):
        self.__defaultValuesSetter = defaultValuesSetter

    def process(self, containerBuild: ContainerBuild):
        for service in containerBuild.services:
            self.__setDefaultValues(service)

    def __setDefaultValues(self, service: Service):
        definition = service.definition

        if definition.usesFactory():
            return

        newArguments = self.__defaultValuesSetter.set(
            definition.arguments,
            service.constructorArguments,
        )

        definition.setArguments(newArguments)
