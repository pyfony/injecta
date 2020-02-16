from abc import ABC, abstractmethod
from injecta.service.class_.ConstructorArgument import ConstructorArgument

class ArgumentInterface(ABC):

    @abstractmethod
    def getStringValue(self):
        pass

    @abstractmethod
    def checkTypeMatchesDefinition(self, constructorArgument: ConstructorArgument, services2Classes: dict):
        pass
