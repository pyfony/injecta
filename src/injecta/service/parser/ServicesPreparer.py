from typing import List, Tuple
from injecta.service.ServiceAlias import ServiceAlias
from injecta.service.parser.ServiceParser import ServiceParser
from injecta.service.Service import Service
from injecta.schema.SchemaValidator import SchemaValidator

class ServicesPreparer:

    def __init__(
        self,
        schemaValidator: SchemaValidator,
        serviceParser: ServiceParser,
    ):
        self.__schemaValidator = schemaValidator
        self.__serviceParser = serviceParser

    def prepare(self, rawDefinitions) -> Tuple[List[Service], List[ServiceAlias]]:
        self.__schemaValidator.validate(rawDefinitions)

        services: List[Service] = []
        aliases: List[ServiceAlias] = []

        for serviceName, rawDefinition in rawDefinitions.items():
            if self.__isServiceAlias(rawDefinition):
                serviceAlias = ServiceAlias(serviceName, rawDefinition[1:])
                aliases.append(serviceAlias)
            else:
                service = self.__serviceParser.parse(serviceName, rawDefinition)
                services.append(service)

        return services, aliases

    def __isServiceAlias(self, rawDefinition: dict):
        return isinstance(rawDefinition, str) and rawDefinition[:1] == '@'
