from abc import ABC

class ConfigReaderInterface(ABC):

    def read(self, configPath: str) -> dict:
        pass
