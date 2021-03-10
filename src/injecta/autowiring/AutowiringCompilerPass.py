from injecta.autowiring.ArgumentsAutowirer import ArgumentsAutowirer
from injecta.compiler.CompilerPassInterface import CompilerPassInterface
from injecta.container.ContainerBuild import ContainerBuild
from injecta.service.resolved.ResolvedService import ResolvedService


class AutowiringCompilerPass(CompilerPassInterface):
    def __init__(self, arguments_autowirer: ArgumentsAutowirer):
        self.__arguments_autowirer = arguments_autowirer

    def process(self, container_build: ContainerBuild):
        def should_autowire(resolved_service: ResolvedService):
            return resolved_service.service.autowire is True and resolved_service.resolved_arguments

        services_for_autowiring = list(filter(should_autowire, container_build.resolved_services))

        for resolved_service in services_for_autowiring:
            self.__autowire(resolved_service, container_build.classes2_services)

    def __autowire(self, resolved_service: ResolvedService, classes2_services: dict):
        resolved_arguments = self.__arguments_autowirer.autowire(
            resolved_service.service.name,
            resolved_service.resolved_arguments,
            classes2_services,
        )

        resolved_service.replace_resolved_arguments(resolved_arguments)
