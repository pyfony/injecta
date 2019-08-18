#pylint: disable = invalid-name, no-member, unused-import, unused-import
from box import Box
import os
from Injecta.ContainerInterface import ContainerInterface
from Injecta.CodeGenerator.ServiceMethodNameTranslator import ServiceMethodNameTranslator
from Injecta.Service.DiService import diService

class Container(ContainerInterface):

    def __init__(self, parameters: Box):
        self.__parameters = parameters
        self.services = {}
        self.__serviceMethodNameTranslator = ServiceMethodNameTranslator()
        self.__tags2Services = self.__generateTags2Services()

    def getConfig(self) -> Box:
        return self.__parameters

    def get(self, name):
        if hasattr(name, '__module__'):
            name = name.__module__

        methodName = self.__serviceMethodNameTranslator.translate(name)
        method = getattr(self, '_Container{}'.format(methodName))

        return method()

    def getByTag(self, tag: str):
        if tag not in self.__tags2Services:
            raise Exception('No service with tag {}'.format(tag))

        serviceNames = self.__tags2Services[tag]

        return list(map(self.get, serviceNames))
