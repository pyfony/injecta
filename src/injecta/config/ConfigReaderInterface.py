from abc import ABC, abstractmethod


class ConfigReaderInterface(ABC):
    @abstractmethod
    def read(self, config_path: str) -> dict:
        pass
