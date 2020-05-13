from typing import List
from injecta.service.ServiceValidatorException import ServiceValidatorException
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

    def getStringValue(self):
        argumentList = list(map(lambda item: item.getStringValue(), self.__items))
        return '[' + ', '.join(argumentList) + ']'

    def checkTypeMatchesDefinition(self, inspectedArgument: InspectedArgument, services2Classes: dict):
        dtype = inspectedArgument.dtype

        if isinstance(dtype, ListTypeInjecta) is False:
            raise ServiceValidatorException(
                inspectedArgument.name,
                'typing.List',
                self.__items.__class__.__name__,
            )

        i = 0
        for item in self.__items:
            inspectedSubArgument = InspectedArgument(inspectedArgument.name + '_' + str(i), inspectedArgument.dtype)

            item.checkTypeMatchesDefinition(inspectedSubArgument, services2Classes)

    def __eq__(self, other: 'ListArgument'):
        return self.name == other.name and self.getStringValue() == other.getStringValue()
