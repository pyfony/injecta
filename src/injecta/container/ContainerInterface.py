from abc import ABC
from box import Box

class ContainerInterface(ABC):

    def getConfig(self) -> Box:
        pass

    def get(self, ident):
        pass
