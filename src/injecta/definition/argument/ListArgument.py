from typing import List
from injecta.service.ServiceValidatorException import ServiceValidatorException
from injecta.dtype.ListType import ListType as ListTypeInjecta
from injecta.definition.argument.ArgumentInterface import ArgumentInterface
from injecta.service.class_.ConstructorArgument import ConstructorArgument

class ListArgument(ArgumentInterface):

    def __init__(self, items: List[ArgumentInterface]):
        self.__items = items

    def getStringValue(self):
        argumentList = list(map(lambda item: item.getStringValue(), self.__items))
        return '[' + ', '.join(argumentList) + ']'

    def checkTypeMatchesDefinition(self, constructorArgument: ConstructorArgument, services2Classes: dict):
        dtype = constructorArgument.dtype

        if isinstance(dtype, ListTypeInjecta) is False:
            raise ServiceValidatorException(
                constructorArgument.name,
                'typing.List',
                self.__items.__class__.__name__,
            )

        i = 0
        for item in self.__items:
            constructorSubArgument = ConstructorArgument(constructorArgument.name + '_' + str(i), constructorArgument.dtype)

            item.checkTypeMatchesDefinition(constructorSubArgument, services2Classes)

    def __eq__(self, other: 'ListArgument'):
        return self.getStringValue() == other.getStringValue()
