from injecta.service.resolved.ArgumentListResolver import ArgumentListResolver
from injecta.service.resolved.NamedArgumentsResolver import NamedArgumentsResolver
from injecta.service.resolved.ResolvedService import ResolvedService
from injecta.service.argument.validator.ArgumentsValidator import ArgumentsValidator
from injecta.service.Service import Service
from injecta.service.class_.InspectedArgumentsResolver import InspectedArgumentsResolver


class ServiceResolver:
    def __init__(self):
        self.__inspected_arguments_resolver = InspectedArgumentsResolver()
        self.__arguments_validator = ArgumentsValidator()
        self.__argument_list_resolver = ArgumentListResolver()
        self.__named_arguments_resolver = NamedArgumentsResolver()

    def resolve(self, service: Service, services2_classes: dict, aliases2_services: dict) -> ResolvedService:
        if service.uses_factory():
            if service.factory_service.service_name not in services2_classes:
                raise Exception(f"Factory service {service.factory_service.service_name} not found")

            factory_class = services2_classes[service.factory_service.service_name]
            inspected_arguments = self.__inspected_arguments_resolver.resolve_method(factory_class, service.factory_method)
        else:
            inspected_arguments = self.__inspected_arguments_resolver.resolve_constructor(service.class_)

        if service.has_named_arguments():
            resolved_arguments = self.__named_arguments_resolver.resolve(service.arguments, inspected_arguments, service.name)
        else:
            resolved_arguments = self.__argument_list_resolver.resolve(service.arguments, inspected_arguments, service.name)

        if not service.uses_factory():
            self.__arguments_validator.validate(service.name, resolved_arguments, services2_classes, aliases2_services)

        return ResolvedService(service, resolved_arguments)
