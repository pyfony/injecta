from injecta.service.argument.ArgumentInterface import ArgumentInterface
from injecta.service.class_.InspectedArgument import InspectedArgument

class DictArgument(ArgumentInterface):

    def __init__(self, value: dict, name: str = None):
        self.__value = value
        self.__name = name

    @property
    def name(self):
        return self.__name

    def getStringValue(self):
        output = []

        for key, subArgument in self.__value.items():
            output.append('{} = {}'.format(key, subArgument.getStringValue()))

        return ', '.join(output)

    def checkTypeMatchesDefinition(self, inspectedArgument: InspectedArgument, services2Classes: dict):
        pass

    def __eq__(self, other: 'DictArgument'):
        return self.name == other.name and self.getStringValue() == other.getStringValue()
