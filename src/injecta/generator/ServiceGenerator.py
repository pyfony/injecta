from injecta.generator.ObjectGenerator import ObjectGenerator
from injecta.generator.ServiceMethodNameTranslator import ServiceMethodNameTranslator
from injecta.service.resolved.ResolvedService import ResolvedService


class ServiceGenerator:
    def __init__(self, object_generator: ObjectGenerator, service_method_name_translator: ServiceMethodNameTranslator):
        self.__object_generator = object_generator
        self.__service_method_name_translator = service_method_name_translator

    def generate(self, resolved_service: ResolvedService):
        method_name = self.__service_method_name_translator.translate(resolved_service.service.name)

        return "    @di_service\n" "    def " + method_name + "(self):\n" "" + self.__object_generator.generate(resolved_service) + "\n"

    def generate_aliases(self, alias: str, service_name: str):
        method_name = self.__service_method_name_translator.translate(alias)
        alias_method_name = self.__service_method_name_translator.translate(service_name)

        return "    @di_service\n" "    def " + method_name + "(self):\n" "        return self." + alias_method_name + "()\n"
