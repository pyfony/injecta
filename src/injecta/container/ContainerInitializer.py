import tempfile
import importlib.util
from injecta.container.ContainerBuild import ContainerBuild
from injecta.container.ContainerInterface import ContainerInterface
from injecta.generator.ContainerGenerator import ContainerGenerator
from injecta.generator.ServiceGenerator import ServiceGenerator
from injecta.generator.ObjectGenerator import ObjectGenerator
from injecta.generator.ServiceMethodNameTranslator import ServiceMethodNameTranslator

class ContainerInitializer:

    def __init__(self):
        self.__containerGenerator = ContainerGenerator(
            ServiceGenerator(
                ObjectGenerator(),
                ServiceMethodNameTranslator()
            ),
        )

    def init(self, containerBuild: ContainerBuild) -> ContainerInterface:
        code = self.__containerGenerator.generate(containerBuild.resolvedServices)

        tmpFile = self.__writeContainer(code)
        module = self.__importContainer(tmpFile.name)
        tmpFile.close()

        return module.Container(containerBuild.parameters)

    def __writeContainer(self, code: str):
        f = tempfile.NamedTemporaryFile(prefix='di_container_', suffix='.py', delete=False)
        f.write(code.encode())
        f.seek(0)

        return f

    def __importContainer(self, filePath):
        spec = importlib.util.spec_from_file_location('container', filePath)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        return module
