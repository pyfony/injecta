from injecta.service.parser.DTypeResolver import DTypeResolver
from injecta.service.argument.ArgumentParser import ArgumentParser
from injecta.service.Service import Service
from injecta.service.argument.ServiceArgument import ServiceArgument


class ServiceParser:
    def __init__(
        self,
        argument_parser: ArgumentParser,
        type_resolver: DTypeResolver,
    ):
        self.__argument_parser = argument_parser
        self.__type_resolver = type_resolver

    def parse(self, service_name: str, raw_service: dict = None):
        if raw_service is None:
            return Service(service_name, self.__type_resolver.resolve(service_name))

        arguments = self.__parse_arguments(raw_service)
        tags = raw_service["tags"] if "tags" in raw_service else []
        class_ = self.__type_resolver.resolve(raw_service["class"] if "class" in raw_service else service_name)

        service = Service(service_name, class_, arguments, tags)

        if "autowire" in raw_service:
            service.set_autowire(raw_service["autowire"] is True)

        if "factory" in raw_service:
            if raw_service["factory"][0][0:1] != "@":
                raise Exception("Factory service name must be prefixed with @ (service {})".format(service_name))

            service.set_factory(ServiceArgument(raw_service["factory"][0][1:]), raw_service["factory"][1])

        return service

    def __parse_arguments(self, raw_service: dict):
        arguments = []

        if "arguments" in raw_service:
            if isinstance(raw_service["arguments"], list):
                arguments = [self.__argument_parser.parse(argument) for argument in raw_service["arguments"]]
            elif isinstance(raw_service["arguments"], dict):
                arguments = [self.__argument_parser.parse(argument, name) for name, argument in raw_service["arguments"].items()]

        return arguments
