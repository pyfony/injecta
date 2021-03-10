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
        self.__container_generator = ContainerGenerator(
            ServiceGenerator(ObjectGenerator(), ServiceMethodNameTranslator()),
        )

    def init(self, container_build: ContainerBuild) -> ContainerInterface:
        code = self.__container_generator.generate(container_build.resolved_services, container_build.aliases2_services)

        tmp_file = self.__write_container(code)
        module = self.__import_container(tmp_file.name)
        tmp_file.close()

        return module.Container(container_build.parameters)

    def __write_container(self, code: str):
        f = tempfile.NamedTemporaryFile(prefix="di_container_", suffix=".py", delete=False)
        f.write(code.encode())
        f.seek(0)

        return f

    def __import_container(self, file_path):
        spec = importlib.util.spec_from_file_location("container", file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        return module
