from injecta.generator.ServiceMethodNameTranslator import ServiceMethodNameTranslator
from injecta.service.argument.ArgumentInterface import ArgumentInterface
from injecta.service.argument.validator.ArgumentsValidatorException import ArgumentsValidatorException
from injecta.service.class_.InspectedArgument import InspectedArgument
from injecta.dtype.DType import DType
from injecta.module import attribute_loader


class ServiceArgument(ArgumentInterface):

    __service_method_translator = ServiceMethodNameTranslator()

    def __init__(self, service_name: str, name: str = None):
        self.__service_name = service_name
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def service_name(self):
        return self.__service_name

    def get_string_value(self):
        return "self." + self.__service_method_translator.translate(self.__service_name) + "()"

    def check_type_matches_definition(self, inspected_argument: InspectedArgument, services2_classes: dict, aliases2_services: dict):
        service_class_type = self.__resolve_service_class_type(services2_classes, aliases2_services)

        if service_class_type == inspected_argument.dtype:
            return

        service_class = attribute_loader.load(service_class_type.module_name, service_class_type.class_name)
        inspected_argument_class = attribute_loader.load(inspected_argument.dtype.module_name, inspected_argument.dtype.class_name)

        if not issubclass(service_class, inspected_argument_class):
            raise ArgumentsValidatorException(inspected_argument.name, str(inspected_argument.dtype), str(service_class_type))

    def __resolve_service_class_type(self, services2_classes: dict, aliases2_services: dict) -> DType:
        if self.__service_name in services2_classes:
            return services2_classes[self.__service_name]

        if self.__service_name in aliases2_services:

            def resolve_recursive(service_name):
                aliased_service_name = aliases2_services[service_name]

                if aliased_service_name in aliases2_services:
                    return resolve_recursive(aliased_service_name)

                if aliased_service_name not in services2_classes:
                    raise Exception(f'Aliased service "{aliased_service_name}" does not exist')

                return services2_classes[aliased_service_name]

            return resolve_recursive(self.__service_name)

        raise Exception(f"Undefined service {self.__service_name}")

    def __eq__(self, other: "ServiceArgument"):
        return self.name == other.name and self.get_string_value() == other.get_string_value()
