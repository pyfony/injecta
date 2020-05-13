from injecta.service.resolved.ArgumentListResolver import ArgumentListResolver
from injecta.service.resolved.NamedArgumentsResolver import NamedArgumentsResolver
from injecta.service.resolved.ResolvedService import ResolvedService
from injecta.service.ServiceValidator import ServiceValidator
from injecta.service.Service import Service
from injecta.service.class_.InspectedArgumentsResolver import InspectedArgumentsResolver

class ServiceResolver:

    def __init__(self):
        self.__inspectedArgumentsResolver = InspectedArgumentsResolver()
        self.__serviceValidator = ServiceValidator()
        self.__argumentListResolver = ArgumentListResolver()
        self.__namedArgumentsResolver = NamedArgumentsResolver()

    def resolve(self, service: Service, services2Classes: dict) -> ResolvedService:
        if service.usesFactory():
            factoryClass = services2Classes[service.factoryService.serviceName]
            inspectedArguments = self.__inspectedArgumentsResolver.resolveMethod(factoryClass, service.factoryMethod)
        else:
            inspectedArguments = self.__inspectedArgumentsResolver.resolveConstructor(service.class_)

        if service.hasNamedArguments():
            resolvedArguments = self.__namedArgumentsResolver.resolve(service.arguments, inspectedArguments, service.name)
        else:
            resolvedArguments = self.__argumentListResolver.resolve(service.arguments, inspectedArguments, service.name)

        if not service.usesFactory():
            self.__serviceValidator.validate(service.name, resolvedArguments, services2Classes)

        return ResolvedService(service, resolvedArguments)
