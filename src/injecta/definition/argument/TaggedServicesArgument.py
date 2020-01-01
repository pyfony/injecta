from injecta.definition.argument.ArgumentInterface import ArgumentInterface
from injecta.service.class_.ConstructorArgument import ConstructorArgument

class TaggedServicesArgument(ArgumentInterface):

    def __init__(self, tagName: str):
        self.__tagName = tagName

    @property
    def tagName(self):
        return self.__tagName

    def getStringValue(self):
        raise Exception('Not implemented')

    def checkTypeMatchesDefinition(self, constructorArgument: ConstructorArgument, services2Classes: dict):
        pass

    def __eq__(self, other: 'TaggedServicesArgument'):
        return self.getStringValue() == other.getStringValue()
