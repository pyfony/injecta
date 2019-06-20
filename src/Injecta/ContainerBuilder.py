from box import Box
import tempfile
import importlib.util
from Injecta.YamlParser import YamlParser
from Injecta.DefinitionParser import DefinitionParser
from Injecta.Autowiring.Autowirer import Autowirer
from Injecta.Autowiring.ArgumentResolver import ArgumentResolver
from Injecta.CodeGenerator.ContainerGenerator import ContainerGenerator
from Injecta.CodeGenerator.ServiceGenerator import ServiceGenerator
from Injecta.CodeGenerator.ObjectGenerator import ObjectGenerator
from Injecta.ClassListBuilder import ClassListBuilder
from Injecta.CodeGenerator.ServiceMethodNameTranslator import ServiceMethodNameTranslator

class ContainerBuilder:

    def build(self, config: Box, servicesConfigPath: str):
        classListBuilder = ClassListBuilder()
        autowirer = Autowirer(ArgumentResolver())
        containerGenerator = ContainerGenerator(ServiceGenerator(ObjectGenerator(), ServiceMethodNameTranslator()))

        definitions = self.__readDefinitions(servicesConfigPath)

        classes = classListBuilder.buildClassList(definitions)

        definitions = list(map(lambda definition: autowirer.autowire(definition, classes), definitions))

        code = containerGenerator.generate(definitions)

        tmpFile = self.__writeContainer(code)
        module = self.__importContainer(tmpFile.name)
        tmpFile.close()

        return module.Container(config)

    def __readDefinitions(self, servicesConfigPath):
        yamlParser = YamlParser(DefinitionParser())

        with open(servicesConfigPath, 'r', encoding='utf-8') as f:
            definitions = yamlParser.parse(f.read())
            f.close()

        return definitions

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
