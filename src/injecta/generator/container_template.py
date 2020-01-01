#pylint: disable = invalid-name, no-member, unused-import, unused-import
from box import Box
import os
from injecta.container.ContainerInterface import ContainerInterface
from injecta.generator.ServiceMethodNameTranslator import ServiceMethodNameTranslator
from injecta.generator.DiService import diService

class Container(ContainerInterface):

    def __init__(self, parameters: Box):
        self.__parameters = parameters
        self.services = {}
        self.__serviceMethodNameTranslator = ServiceMethodNameTranslator()

    def getConfig(self) -> Box:
        return self.__parameters

    def get(self, ident):
        if isinstance(ident, str):
            method = getattr(self, '_Container{}'.format(self.__serviceMethodNameTranslator.translate(ident)))

            return method()

        # service: foo.bar.HelloClass, class: foo.bar.HelloClass
        name = ident.__module__ + '.' + ident.__name__
        methodName = '_Container{}'.format(self.__serviceMethodNameTranslator.translate(name))

        if hasattr(self, methodName):
            method = getattr(self, methodName)

            return method()

        # service: foo.bar.HelloClass, class: foo.bar.HelloClass.HelloClass
        name = ident.__module__
        methodName = '_Container{}'.format(self.__serviceMethodNameTranslator.translate(name))

        if hasattr(self, methodName):
            method = getattr(self, methodName)

            service = method()

            if not isinstance(service, ident):
                raise Exception('Resolved service {} expected to be instance of {}'.format(service, ident))

            return service

        raise Exception('Cannot find service for: {}'.format(ident))
