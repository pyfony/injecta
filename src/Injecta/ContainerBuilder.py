from box import Box
import tempfile
import importlib.util
from Injecta.Autowiring.Autowirer import Autowirer
from Injecta.Autowiring.ArgumentResolver import ArgumentResolver
from Injecta.CodeGenerator.ContainerGenerator import ContainerGenerator
from Injecta.CodeGenerator.ServiceGenerator import ServiceGenerator
from Injecta.CodeGenerator.ObjectGenerator import ObjectGenerator
from Injecta.CodeGenerator.Tags2ServicesPreparer import Tags2ServicesPreparer
from Injecta.ClassListBuilder import ClassListBuilder
from Injecta.CodeGenerator.ServiceMethodNameTranslator import ServiceMethodNameTranslator

class ContainerBuilder:

    def __init__(self):
        self.__classListBuilder = ClassListBuilder()
        self.__autowirer = Autowirer(ArgumentResolver())
        self.__containerGenerator = ContainerGenerator(
            ServiceGenerator(
                ObjectGenerator(),
                ServiceMethodNameTranslator()
            ),
            Tags2ServicesPreparer()
        )

    def build(self, config: Box, definitions: list):
        classes = self.__classListBuilder.buildClassList(definitions)

        definitions = list(map(lambda definition: self.__autowirer.autowire(definition, classes), definitions))

        code = self.__containerGenerator.generate(definitions)

        tmpFile = self.__writeContainer(code)
        module = self.__importContainer(tmpFile.name)
        tmpFile.close()

        return module.Container(config)

    def __writeContainer(self, code: str):
        f = tempfile.NamedTemporaryFile(prefix='di_container_', suffix='.py')
        f.write(code.encode())
        f.seek(0)

        return f

    def __importContainer(self, filePath):
        spec = importlib.util.spec_from_file_location('Container', filePath)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        return module
