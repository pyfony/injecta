from injecta.service.argument.ArgumentInterface import ArgumentInterface
from injecta.service.class_.InspectedArgument import InspectedArgument

class TaggedServicesArgument(ArgumentInterface):

    def __init__(self, tagName: str, name: str = None):
        self.__tagName = tagName
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def tagName(self):
        return self.__tagName

    def getStringValue(self):
        raise Exception('TaggedServicesCompilerPass probably failed to convert tagged arguments')

    def checkTypeMatchesDefinition(self, inspectedArgument: InspectedArgument, services2Classes: dict):
        pass

    def __eq__(self, other: 'TaggedServicesArgument'):
        return self.name == other.name and self.getStringValue() == other.getStringValue()
