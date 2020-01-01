from injecta.definition.argument.ArgumentInterface import ArgumentInterface
from injecta.service.class_.ConstructorArgument import ConstructorArgument

class DictArgument(ArgumentInterface):

    def __init__(self, value: dict):
        self.__value = value

    def getStringValue(self):
        output = []

        for key, subArgument in self.__value.items():
            output.append('{} = {}'.format(key, subArgument.getStringValue()))

        return ', '.join(output)

    def checkTypeMatchesDefinition(self, constructorArgument: ConstructorArgument, services2Classes: dict):
        pass

    def __eq__(self, other: 'DictArgument'):
        return self.getStringValue() == other.getStringValue()
