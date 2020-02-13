from typing import List
from injecta.service.ServiceParser import ServiceParser
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

    def prepare(self, rawServices) -> List[Service]:
        self.__schemaValidator.validate(rawServices)

        return list(self.__serviceParser.parse(name, service) for name, service in rawServices.items())
