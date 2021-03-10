from abc import ABC, abstractmethod
from injecta.service.class_.InspectedArgument import InspectedArgument


class ArgumentInterface(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def get_string_value(self):
        pass

    @abstractmethod
    def check_type_matches_definition(self, inspected_argument: InspectedArgument, services2_classes: dict, aliases2_services: dict):
        pass
