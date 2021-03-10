from typing import List
from injecta.autowiring.ArgumentResolver import ArgumentResolver
from injecta.container.ContainerInterface import ContainerInterface
from injecta.service.argument.ServiceArgument import ServiceArgument
from injecta.service.resolved.ResolvedArgument import ResolvedArgument


class ArgumentsAutowirer:
    def __init__(self, argument_resolver: ArgumentResolver):
        self.__argument_resolver = argument_resolver

    def autowire(self, service_name: str, resolved_arguments: List[ResolvedArgument], classes2_services: dict):
        def autowire_argument(resolved_argument: ResolvedArgument):
            if resolved_argument.argument or resolved_argument.inspected_argument.has_default_value():
                return resolved_argument

            if resolved_argument.inspected_argument.dtype.module_name == ContainerInterface.__module__:
                service_argument = ServiceArgument("service_container", resolved_argument.name)
                resolved_argument.modify_argument(service_argument, "container autowiring")

                return resolved_argument

            service_argument = self.__argument_resolver.resolve(resolved_argument.inspected_argument, service_name, classes2_services)
            resolved_argument.modify_argument(service_argument, "autowiring")

            return resolved_argument

        return list(map(autowire_argument, resolved_arguments))
