from injecta.service.resolved.ResolvedService import ResolvedService
from injecta.service.ServiceValidator import ServiceValidator
from injecta.service.Service import Service
from injecta.service.class_.InspectedArgumentsResolver import InspectedArgumentsResolver

class ServiceResolver:

    def __init__(self):
        self.__inspectedArgumentsResolver = InspectedArgumentsResolver()
        self.__serviceValidator = ServiceValidator()

    def resolve(self, service: Service, services2Classes: dict) -> ResolvedService:
        inspectedArguments = self.__inspectedArgumentsResolver.resolve(service.class_)

        if service.usesFactory() is False:
            self.__serviceValidator.validate(
                service.name,
                service.arguments,
                inspectedArguments,
                services2Classes
            )

        return ResolvedService(service, inspectedArguments)
