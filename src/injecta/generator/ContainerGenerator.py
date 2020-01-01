from typing import List
from injecta.generator.ServiceGenerator import ServiceGenerator
from injecta.definition.Definition import Definition
from injecta.libRoot import getLibRoot

class ContainerGenerator:

    def __init__(self,
        serviceGenerator: ServiceGenerator,
    ):
        self.__serviceGenerator = serviceGenerator

    def generate(self, definitions: List[Definition]):
        path = getLibRoot() + '/generator/container_template.py'

        with open(path, 'r', encoding='utf-8') as f:
            output = f.read() + '\n'
            f.close()

        codeOfServiceMethods = list(map(self.__serviceGenerator.generate, definitions))

        output += '\n'.join(codeOfServiceMethods)

        return output
