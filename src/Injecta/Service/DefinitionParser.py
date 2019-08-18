from Injecta.Argument.ArgumentParser import ArgumentParser
from Injecta.Module.ModuleClassResolver import ModuleClassResolver
from Injecta.Service.Definition import Definition
from Injecta.Argument.ServiceArgument import ServiceArgument

class DefinitionParser:

    def __init__(
        self,
        argumentParser: ArgumentParser,
        moduleClassResolver: ModuleClassResolver
    ):
        self.__argumentParser = argumentParser
        self.__moduleClassResolver = moduleClassResolver

    def parse(self, serviceName: str, serviceDefinition: dict):
        if serviceDefinition is None:
            moduleClass = self.__moduleClassResolver.resolve(serviceName)
            return Definition(serviceName, moduleClass)

        arguments = self.__parseArguments(serviceDefinition)
        tags = serviceDefinition['tags'] if 'tags' in serviceDefinition else []
        classFqn = serviceDefinition['class'] if 'class' in serviceDefinition else serviceName

        moduleClass = self.__moduleClassResolver.resolve(classFqn)

        definition = Definition(serviceName, moduleClass, arguments, tags)

        if 'autowire' in serviceDefinition:
            definition.setAutowire(serviceDefinition['autowire'] == 'True')

        if 'factory' in serviceDefinition:
            if serviceDefinition['factory'][0][0:1] != '@':
                raise Exception('Factory service name must be prefixed with @ (service {})'.format(serviceName))

            definition.setFactory(
                ServiceArgument(serviceDefinition['factory'][0][1:]),
                serviceDefinition['factory'][1]
            )

        return definition

    def __parseArguments(self, serviceDefinition):
        arguments = []

        if 'arguments' in serviceDefinition:
            arguments = list(map(self.__argumentParser.parse, serviceDefinition['arguments']))

        return arguments
