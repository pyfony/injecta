from abc import ABC, abstractmethod

class ConfigReaderInterface(ABC):

    @abstractmethod
    def read(self, configPath: str) -> dict:
        pass
