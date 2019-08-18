from abc import ABC
from box import Box

class ContainerInterface(ABC):

    def getConfig(self) -> Box:
        pass

    def get(self, name):
        pass

    def getByTag(self, tag: str):
        pass
