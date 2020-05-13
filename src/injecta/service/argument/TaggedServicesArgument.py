from injecta.service.argument.ArgumentInterface import ArgumentInterface
from injecta.service.class_.InspectedArgument import InspectedArgument

class TaggedServicesArgument(ArgumentInterface):

    def __init__(self, tagName: str):
        self.__tagName = tagName

    @property
    def tagName(self):
        return self.__tagName

    def getStringValue(self):
        raise Exception('Not implemented')

    def checkTypeMatchesDefinition(self, inspectedArgument: InspectedArgument, services2Classes: dict):
        pass

    def __eq__(self, other: 'TaggedServicesArgument'):
        return self.getStringValue() == other.getStringValue()
