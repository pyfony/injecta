from injecta.service.argument.ArgumentInterface import ArgumentInterface
from injecta.service.class_.InspectedArgument import InspectedArgument


class DictArgument(ArgumentInterface):
    def __init__(self, value: dict, name: str = None):
        self.__value = value
        self.__name = name

    @property
    def name(self):
        return self.__name

    def get_string_value(self):
        output = []

        for key, sub_argument in self.__value.items():
            output.append("{} = {}".format(key, sub_argument.get_string_value()))

        return ", ".join(output)

    def check_type_matches_definition(self, inspected_argument: InspectedArgument, services2_classes: dict, aliases2_services: dict):
        pass

    def __eq__(self, other: "DictArgument"):
        return self.name == other.name and self.get_string_value() == other.get_string_value()
