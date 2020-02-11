import os
from typing import List
from injecta.InjectaBundle import InjectaBundle
from injecta.bundle.Bundle import Bundle
from injecta.bundle.BundleManager import BundleManager
from injecta.generator.Tag2DefinitionsPreparer import Tag2DefinitionsPreparer
from injecta.compiler.CompilerPassInterface import CompilerPassInterface
from injecta.container.ContainerBuild import ContainerBuild
from injecta.definition.DefinitionsPreparer import DefinitionsPreparer
from injecta.definition.DTypeResolver import DTypeResolver
from injecta.parameter.ParametersParser import ParametersParser
from injecta.service.Classes2ServicesBuilder import Classes2ServicesBuilder
from injecta.autowiring.ArgumentResolver import ArgumentResolver
from injecta.autowiring.ArgumentsAutowirer import ArgumentsAutowirer
from injecta.service.Service import Service
from injecta.service.ServiceResolver import ServiceResolver
from injecta.definition.DefinitionParser import DefinitionParser
from injecta.definition.argument.ArgumentParser import ArgumentParser
from injecta.schema.SchemaValidator import SchemaValidator

class ContainerBuilder:

    def __init__(self):
        self.__classes2ServicesBuilder = Classes2ServicesBuilder()
        self.__definitionsPreparer = DefinitionsPreparer(
            SchemaValidator(),
            DefinitionParser(
                ArgumentParser(),
                DTypeResolver(),
            )
        )
        self.__servicesResolver = ServiceResolver()
        self.__autowirer = ArgumentsAutowirer(
            ArgumentResolver()
        )
        self.__parametersParser = ParametersParser()
        self.__tag2DefinitionsPreparer = Tag2DefinitionsPreparer()

    def build(self, appRawConfig: dict, bundles: List[Bundle], appEnv: str, configPath: str) -> ContainerBuild:
        bundleManager = BundleManager([InjectaBundle()] + bundles)

        rawConfig = bundleManager.mergeRawConfig(appRawConfig)
        rawConfig = bundleManager.modifyRawConfig(rawConfig)

        definitions = self.__definitionsPreparer.prepare(rawConfig['services'])
        definitions = bundleManager.modifyDefinitions(definitions)

        classes2Services = self.__classes2ServicesBuilder.build(definitions)
        services2Classes = dict(map(lambda definition: (definition.name, definition.class_), definitions))

        services = list(map(lambda definition: self.__servicesResolver.resolve(definition, services2Classes), definitions)) # type: List[Service]

        tag2Definitions = self.__tag2DefinitionsPreparer.prepare(definitions)

        parameters = self.__parametersParser.parse(rawConfig['parameters'], {
            'project': {
                'configDir': os.path.dirname(configPath),
            },
            'kernel': {
                'environment': appEnv,
            },
        })

        parameters = bundleManager.modifyParameters(parameters)

        containerBuild = ContainerBuild(parameters, services, classes2Services, tag2Definitions, appEnv)

        for compilerPass in bundleManager.getCompilerPasses(): # type: CompilerPassInterface
            compilerPass.process(containerBuild)

        return containerBuild
