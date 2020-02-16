from abc import ABC, abstractmethod
from injecta.container.ContainerBuild import ContainerBuild

class CompilerPassInterface(ABC):

    @abstractmethod
    def process(self, containerBuild: ContainerBuild):
        pass
