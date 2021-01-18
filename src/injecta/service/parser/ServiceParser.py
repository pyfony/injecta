from injecta.service.parser.DTypeResolver import DTypeResolver
from injecta.service.argument.ArgumentParser import ArgumentParser
from injecta.service.Service import Service
from injecta.service.argument.ServiceArgument import ServiceArgument

class ServiceParser:

    def __init__(
        self,
        argumentParser: ArgumentParser,
        typeResolver: DTypeResolver,
    ):
        self.__argumentParser = argumentParser
        self.__typeResolver = typeResolver

    def parse(self, serviceName: str, rawService: dict = None):
        if rawService is None:
            return Service(serviceName, self.__typeResolver.resolve(serviceName))

        arguments = self.__parseArguments(rawService)
        tags = rawService['tags'] if 'tags' in rawService else []
        class_ = self.__typeResolver.resolve(rawService['class'] if 'class' in rawService else serviceName)  # pylint: disable = invalid-name

        service = Service(serviceName, class_, arguments, tags)

        if 'autowire' in rawService:
            service.setAutowire(rawService['autowire'] is True)

        if 'factory' in rawService:
            if rawService['factory'][0][0:1] != '@':
                raise Exception('Factory service name must be prefixed with @ (service {})'.format(serviceName))

            service.setFactory(
                ServiceArgument(rawService['factory'][0][1:]),
                rawService['factory'][1]
            )

        return service

    def __parseArguments(self, rawService: dict):
        arguments = []

        if 'arguments' in rawService:
            if isinstance(rawService['arguments'], list):
                arguments = [self.__argumentParser.parse(argument) for argument in rawService['arguments']]
            elif isinstance(rawService['arguments'], dict):
                arguments = [self.__argumentParser.parse(argument, name) for name, argument in rawService['arguments'].items()]

        return arguments
