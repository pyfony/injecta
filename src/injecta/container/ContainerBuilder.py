from typing import List
from box import Box
from injecta.autowiring.ArgumentResolver import ArgumentResolver
from injecta.autowiring.ArgumentsAutowirer import ArgumentsAutowirer
from injecta.autowiring.AutowiringCompilerPass import AutowiringCompilerPass
from injecta.container.Hooks import Hooks
from injecta.generator.Tag2ServicesPreparer import Tag2ServicesPreparer
from injecta.container.ContainerBuild import ContainerBuild
from injecta.service.Service import Service
from injecta.service.ServiceAlias import ServiceAlias
from injecta.service.parser.ServicesPreparer import ServicesPreparer
from injecta.service.parser.DTypeResolver import DTypeResolver
from injecta.parameter.ParametersParser import ParametersParser
from injecta.service.Classes2ServicesBuilder import Classes2ServicesBuilder
from injecta.service.resolved.ResolvedService import ResolvedService
from injecta.service.resolved.ServiceResolver import ServiceResolver
from injecta.service.parser.ServiceParser import ServiceParser
from injecta.service.argument.ArgumentParser import ArgumentParser
from injecta.schema.SchemaValidator import SchemaValidator
from injecta.service.argument.YamlTagArgumentsCompilerPass import YamlTagArgumentsCompilerPass


class ContainerBuilder:
    def __init__(self):
        self.__classes2_services_builder = Classes2ServicesBuilder()
        self.__services_preparer = ServicesPreparer(
            SchemaValidator(),
            ServiceParser(
                ArgumentParser(),
                DTypeResolver(),
            ),
        )
        self.__services_resolver = ServiceResolver()
        self.__parameters_parser = ParametersParser()
        self.__tag2_services_preparer = Tag2ServicesPreparer()
        self.__default_compiler_passes = [
            YamlTagArgumentsCompilerPass(),
            AutowiringCompilerPass(ArgumentsAutowirer(ArgumentResolver())),
        ]

    def build(self, raw_config: dict, hooks: Hooks = Hooks()) -> ContainerBuild:
        if "parameters" not in raw_config or raw_config["parameters"] is None:
            raw_config["parameters"] = dict()
        if "services" not in raw_config or raw_config["services"] is None:
            raw_config["services"] = dict()

        raw_config = hooks.start(raw_config)

        parameters = self.__parameters_parser.parse(raw_config["parameters"], hooks.get_custom_parameters())
        parameters = hooks.parameters_parsed(parameters)

        services, aliases = self.__services_preparer.prepare(raw_config["services"])
        services, aliases = hooks.services_prepared(services, aliases, parameters)

        container_build = self._build(parameters, services, aliases)

        for compiler_pass in self.__default_compiler_passes:
            compiler_pass.process(container_build)

        hooks.container_build_ready(container_build)

        return container_build

    def _build(self, parameters: Box, services: List[Service], aliases: List[ServiceAlias]):
        aliases2_services = {service_alias.name: service_alias.aliased_service for service_alias in aliases}
        classes2_services = self.__classes2_services_builder.build(services)
        services2_classes = {service.name: service.class_ for service in services}

        resolved_services: List[ResolvedService] = [
            self.__services_resolver.resolve(service, services2_classes, aliases2_services) for service in services
        ]

        tag2_services = self.__tag2_services_preparer.prepare(services)

        return ContainerBuild(parameters, resolved_services, classes2_services, aliases2_services, tag2_services)
