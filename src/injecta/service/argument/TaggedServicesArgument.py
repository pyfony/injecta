from injecta.service.argument.ArgumentInterface import ArgumentInterface
from injecta.service.class_.InspectedArgument import InspectedArgument


class TaggedServicesArgument(ArgumentInterface):
    def __init__(self, tag_name: str, name: str = None):
        self.__tag_name = tag_name
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def tag_name(self):
        return self.__tag_name

    def get_string_value(self):
        raise Exception("YamlTagArgumentsCompilerPass probably failed to convert tagged arguments")

    def check_type_matches_definition(self, inspected_argument: InspectedArgument, services2_classes: dict, aliases2_services: dict):
        pass

    def __eq__(self, other: "TaggedServicesArgument"):
        return self.name == other.name and self.get_string_value() == other.get_string_value()
