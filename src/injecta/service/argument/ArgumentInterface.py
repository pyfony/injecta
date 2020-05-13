from abc import ABC, abstractmethod
from injecta.service.class_.InspectedArgument import InspectedArgument

class ArgumentInterface(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def getStringValue(self):
        pass

    @abstractmethod
    def checkTypeMatchesDefinition(self, inspectedArgument: InspectedArgument, services2Classes: dict):
        pass
