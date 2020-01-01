from injecta.definition.DTypeResolver import DTypeResolver
from injecta.definition.argument.ArgumentParser import ArgumentParser
from injecta.definition.Definition import Definition
from injecta.definition.argument.ServiceArgument import ServiceArgument

class DefinitionParser:

    def __init__(
        self,
        argumentParser: ArgumentParser,
        typeResolver: DTypeResolver,
    ):
        self.__argumentParser = argumentParser
        self.__typeResolver = typeResolver

    def parse(self, serviceName: str, rawDefinition: dict = None):
        if rawDefinition is None:
            return Definition(serviceName, self.__typeResolver.resolve(serviceName))

        arguments = self.__parseArguments(rawDefinition)
        tags = rawDefinition['tags'] if 'tags' in rawDefinition else []
        class_ = self.__typeResolver.resolve(rawDefinition['class'] if 'class' in rawDefinition else serviceName)  # pylint: disable = invalid-name

        definition = Definition(serviceName, class_, arguments, tags)

        if 'autowire' in rawDefinition:
            definition.setAutowire(rawDefinition['autowire'] is True)

        if 'factory' in rawDefinition:
            if rawDefinition['factory'][0][0:1] != '@':
                raise Exception('Factory service name must be prefixed with @ (service {})'.format(serviceName))

            definition.setFactory(
                ServiceArgument(rawDefinition['factory'][0][1:]),
                rawDefinition['factory'][1]
            )

        return definition

    def __parseArguments(self, rawDefinition: dict):
        arguments = []

        if 'arguments' in rawDefinition:
            arguments = list(map(self.__argumentParser.parse, rawDefinition['arguments']))

        return arguments
