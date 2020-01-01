from abc import ABC
from injecta.container.ContainerBuild import ContainerBuild

class CompilerPassInterface(ABC):

    def process(self, containerBuild: ContainerBuild):
        pass
