from typing import List
from injecta.autowiring.ArgumentResolver import ArgumentResolver
from injecta.autowiring.ArgumentsAutowirer import ArgumentsAutowirer
from injecta.autowiring.AutowiringCompilerPass import AutowiringCompilerPass
from injecta.container.Hooks import Hooks
from injecta.generator.Tag2ServicesPreparer import Tag2ServicesPreparer
from injecta.container.ContainerBuild import ContainerBuild
from injecta.service.ServicesPreparer import ServicesPreparer
from injecta.service.DTypeResolver import DTypeResolver
from injecta.parameter.ParametersParser import ParametersParser
from injecta.service.Classes2ServicesBuilder import Classes2ServicesBuilder
from injecta.service.resolved.ResolvedService import ResolvedService
from injecta.service.resolved.ServiceResolver import ServiceResolver
from injecta.service.ServiceParser import ServiceParser
from injecta.service.argument.ArgumentParser import ArgumentParser
from injecta.schema.SchemaValidator import SchemaValidator
from injecta.tag.TaggedServicesCompilerPass import TaggedServicesCompilerPass

class ContainerBuilder:

    def __init__(self):
        self.__classes2ServicesBuilder = Classes2ServicesBuilder()
        self.__servicesPreparer = ServicesPreparer(
            SchemaValidator(),
            ServiceParser(
                ArgumentParser(),
                DTypeResolver(),
            )
        )
        self.__servicesResolver = ServiceResolver()
        self.__parametersParser = ParametersParser()
        self.__tag2ServicesPreparer = Tag2ServicesPreparer()
        self.__defaultCompilerPasses = [
            TaggedServicesCompilerPass(),
            AutowiringCompilerPass(ArgumentsAutowirer(ArgumentResolver())),
        ]

    def build(self, rawConfig: dict, hooks: Hooks = Hooks()) -> ContainerBuild:
        if 'parameters' not in rawConfig:
            rawConfig['parameters'] = dict()
        if 'services' not in rawConfig:
            rawConfig['services'] = dict()

        rawConfig = hooks.start(rawConfig)

        services = self.__servicesPreparer.prepare(rawConfig['services'])
        services = hooks.servicesPrepared(services)

        classes2Services = self.__classes2ServicesBuilder.build(services)
        services2Classes = dict(map(lambda service: (service.name, service.class_), services))

        resolvedServices = list(map(lambda service: self.__servicesResolver.resolve(service, services2Classes), services)) # type: List[ResolvedService]

        tag2Services = self.__tag2ServicesPreparer.prepare(services)

        parameters = self.__parametersParser.parse(rawConfig['parameters'], hooks.getCustomParameters())
        parameters = hooks.parametersParsed(parameters)

        containerBuild = ContainerBuild(parameters, resolvedServices, classes2Services, tag2Services)

        for compilerPass in self.__defaultCompilerPasses:
            compilerPass.process(containerBuild)

        hooks.containerBuildReady(containerBuild)

        return containerBuild
