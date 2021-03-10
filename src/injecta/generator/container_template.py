from box import Box
import os  # noqa: F401
from injecta.container.ContainerInterface import ContainerInterface
from injecta.generator.ServiceMethodNameTranslator import ServiceMethodNameTranslator
from injecta.generator.DiService import di_service  # noqa: F401


class Container(ContainerInterface):
    def __init__(self, parameters: Box):
        self.__parameters = parameters
        self.services = {}
        self.__service_method_name_translator = ServiceMethodNameTranslator()

    def get_parameters(self) -> Box:
        return self.__parameters

    def get(self, ident):
        if isinstance(ident, str):
            return self.get_by_ident(ident)

        # service: foo.bar.HelloClass, class: foo.bar.HelloClass
        name = ident.__module__ + "." + ident.__name__
        method_name = "_Container{}".format(self.__service_method_name_translator.translate(name))

        if hasattr(self, method_name):
            try:
                method = getattr(self, method_name)
            except AttributeError:
                raise Exception(f"Service {name} not found")

            return method()

        # service: foo.bar.HelloClass, class: foo.bar.HelloClass.HelloClass
        name = ident.__module__
        method_name = "_Container{}".format(self.__service_method_name_translator.translate(name))

        if hasattr(self, method_name):
            try:
                method = getattr(self, method_name)
            except AttributeError:
                raise Exception(f"Service {name} not found")

            service = method()

            if not isinstance(service, ident):
                raise Exception("Resolved service {} expected to be instance of {}".format(service, ident))

            return service

        raise Exception("Cannot find service for: {}".format(ident))

    def get_by_ident(self, ident: str):
        try:
            method = getattr(self, "_Container{}".format(self.__service_method_name_translator.translate(ident)))
        except AttributeError:
            raise Exception(f"Service {ident} not found")

        return method()

    def _Container__service_container(self):  # noqa: 802
        return self
