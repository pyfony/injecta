from typing import List, Tuple
from injecta.service.ServiceAlias import ServiceAlias
from injecta.service.parser.ServiceParser import ServiceParser
from injecta.service.Service import Service
from injecta.schema.SchemaValidator import SchemaValidator


class ServicesPreparer:
    def __init__(
        self,
        schema_validator: SchemaValidator,
        service_parser: ServiceParser,
    ):
        self.__schema_validator = schema_validator
        self.__service_parser = service_parser

    def prepare(self, raw_definitions) -> Tuple[List[Service], List[ServiceAlias]]:
        self.__schema_validator.validate(raw_definitions)

        services: List[Service] = []
        aliases: List[ServiceAlias] = []

        for service_name, raw_definition in raw_definitions.items():
            if self.__is_service_alias(raw_definition):
                service_alias = ServiceAlias(service_name, raw_definition[1:])
                aliases.append(service_alias)
            else:
                service = self.__service_parser.parse(service_name, raw_definition)
                services.append(service)

        return services, aliases

    def __is_service_alias(self, raw_definition: dict):
        return isinstance(raw_definition, str) and raw_definition[:1] == "@"
