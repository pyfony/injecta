from injecta.service.resolved.ResolvedService import ResolvedService
from injecta.service.ServiceValidator import ServiceValidator
from injecta.service.Service import Service
from injecta.service.class_.ConstructorArgumentsResolver import ConstructorArgumentsResolver

class ServiceResolver:

    def __init__(self):
        self.__constructorArgumentsResolver = ConstructorArgumentsResolver()
        self.__serviceValidator = ServiceValidator()

    def resolve(self, service: Service, services2Classes: dict) -> ResolvedService:
        constructorArguments = self.__constructorArgumentsResolver.resolve(service.class_)

        if service.usesFactory() is False:
            self.__serviceValidator.validate(
                service.name,
                service.arguments,
                constructorArguments,
                services2Classes
            )

        return ResolvedService(service, constructorArguments)
