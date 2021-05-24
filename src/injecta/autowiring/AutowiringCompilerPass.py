from injecta.autowiring.ArgumentsAutowirer import ArgumentsAutowirer
from injecta.compiler.CompilerPassInterface import CompilerPassInterface
from injecta.container.ContainerBuild import ContainerBuild
from injecta.service.resolved.ResolvedService import ResolvedService


class AutowiringCompilerPass(CompilerPassInterface):
    def __init__(self, arguments_autowirer: ArgumentsAutowirer):
        self.__arguments_autowirer = arguments_autowirer

    def process(self, container_build: ContainerBuild):
        to_autowire = []

        def should_autowire(resolved_service: ResolvedService):
            return resolved_service.service.autowire is True and resolved_service.resolved_arguments

        for resolved_service in container_build.resolved_services:
            if should_autowire(resolved_service):
                to_autowire.append(resolved_service)
            else:
                self.__check_skipped(resolved_service)

        for resolved_service in to_autowire:
            self.__autowire(resolved_service, container_build.classes2_services)

    def __check_skipped(self, resolved_service: ResolvedService):
        if len(resolved_service.service.arguments) < len(resolved_service.resolved_arguments):
            raise Exception(f'Too few arguments given for service "{resolved_service.service.name}"')

    def __autowire(self, resolved_service: ResolvedService, classes2_services: dict):
        resolved_arguments = self.__arguments_autowirer.autowire(
            resolved_service.service.name,
            resolved_service.resolved_arguments,
            classes2_services,
        )

        resolved_service.replace_resolved_arguments(resolved_arguments)
