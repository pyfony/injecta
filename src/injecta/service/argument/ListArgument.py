from typing import List
from injecta.service.argument.validator.ArgumentsValidatorException import ArgumentsValidatorException
from injecta.dtype.ListType import ListType as ListTypeInjecta
from injecta.service.argument.ArgumentInterface import ArgumentInterface
from injecta.service.class_.InspectedArgument import InspectedArgument


class ListArgument(ArgumentInterface):
    def __init__(self, items: List[ArgumentInterface], name: str = None):
        self.__items = items
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def items(self):
        return self.__items

    def get_string_value(self):
        argument_list = list(map(lambda item: item.get_string_value(), self.__items))
        return "[" + ", ".join(argument_list) + "]"

    def check_type_matches_definition(self, inspected_argument: InspectedArgument, services2_classes: dict, aliases2_services: dict):
        dtype = inspected_argument.dtype

        if isinstance(dtype, ListTypeInjecta) is False:
            raise ArgumentsValidatorException(
                inspected_argument.name,
                "typing.List",
                self.__items.__class__.__name__,
            )

        i = 0
        for item in self.__items:
            inspected_sub_argument = InspectedArgument(inspected_argument.name + "_" + str(i), inspected_argument.dtype)

            item.check_type_matches_definition(inspected_sub_argument, services2_classes, aliases2_services)

    def __eq__(self, other: "ListArgument"):
        return self.name == other.name and self.get_string_value() == other.get_string_value()
