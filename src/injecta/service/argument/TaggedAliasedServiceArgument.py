from injecta.service.argument.ArgumentInterface import ArgumentInterface
from injecta.service.class_.InspectedArgument import InspectedArgument

class TaggedAliasedServiceArgument(ArgumentInterface):

    def __init__(self, tagName: str, tagAlias: str, name: str = None):
        self.__tagName = tagName
        self.__tagAlias = tagAlias
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def tagName(self):
        return self.__tagName

    @property
    def tagAlias(self):
        return self.__tagAlias

    def getStringValue(self):
        raise Exception('YamlTagArgumentsCompilerPass probably failed to convert tagged arguments')

    def checkTypeMatchesDefinition(self, inspectedArgument: InspectedArgument, services2Classes: dict, aliases2Services: dict):
        pass

    def __eq__(self, other: 'TaggedAliasedServiceArgument'):
        return self.name == other.name and self.getStringValue() == other.getStringValue()
