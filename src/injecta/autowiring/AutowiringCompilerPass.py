from injecta.autowiring.ArgumentsAutowirer import ArgumentsAutowirer
from injecta.compiler.CompilerPassInterface import CompilerPassInterface
from injecta.container.ContainerBuild import ContainerBuild
from injecta.service.Service import Service

class AutowiringCompilerPass(CompilerPassInterface):

    def __init__(self, argumentsAutowirer: ArgumentsAutowirer):
        self.__argumentsAutowirer = argumentsAutowirer

    def process(self, containerBuild: ContainerBuild):
        servicesForAutowiring = list(filter(lambda service: service.definition.autowire is True and service.constructorArguments, containerBuild.services))

        for service in servicesForAutowiring:
            self.__autowire(service, containerBuild.classes2Services)

    def __autowire(self, service: Service, classes2Services: dict):
        definition = service.definition

        newArguments = self.__argumentsAutowirer.autowire(
            definition.name,
            definition.arguments,
            service.constructorArguments,
            classes2Services,
        )

        definition.setArguments(newArguments)
