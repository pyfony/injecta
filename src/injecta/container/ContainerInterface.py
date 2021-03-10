from abc import ABC
from box import Box


class ContainerInterface(ABC):
    def get_parameters(self) -> Box:
        pass

    def get(self, ident):
        pass
