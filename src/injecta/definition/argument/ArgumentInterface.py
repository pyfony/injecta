from abc import ABC
from injecta.service.class_.ConstructorArgument import ConstructorArgument

class ArgumentInterface(ABC):

    def getStringValue(self):
        pass

    def checkTypeMatchesDefinition(self, constructorArgument: ConstructorArgument, services2Classes: dict):
        pass
