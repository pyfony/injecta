from box import Box
import tempfile
import importlib.util
from typing import List
from Injecta.ContainerBuilder import ContainerBuilder
from Injecta.ContainerInterface import ContainerInterface
from Injecta.Service.Definition import Definition

class ContainerInitializer:

    def __init__(self):
        self.__containerBuilder = ContainerBuilder()

    def init(self, parameters: Box, definitions: List[Definition]) -> ContainerInterface:
        code = self.__containerBuilder.build(definitions)

        tmpFile = self.__writeContainer(code)
        module = self.__importContainer(tmpFile.name)
        tmpFile.close()

        return module.Container(parameters)

    def __writeContainer(self, code: str):
        f = tempfile.NamedTemporaryFile(prefix='di_container_', suffix='.py', delete=False)
        f.write(code.encode())
        f.seek(0)

        return f

    def __importContainer(self, filePath):
        spec = importlib.util.spec_from_file_location('Container', filePath)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        return module
