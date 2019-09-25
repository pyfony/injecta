import json
from typing import List
from Injecta.CodeGenerator.ServiceGenerator import ServiceGenerator
from Injecta.CodeGenerator.Tags2ServicesPreparer import Tags2ServicesPreparer
from Injecta.LibRoot import getLibRoot
from Injecta.Service import Definition

class ContainerGenerator:

    def __init__(self,
        serviceGenerator: ServiceGenerator,
        tags2ServicesPreparer: Tags2ServicesPreparer
    ):
        self.__serviceGenerator = serviceGenerator
        self.__tags2ServicesPreparer = tags2ServicesPreparer

    def generate(self, definitions: List[Definition]):
        path = getLibRoot() + '/CodeGenerator/container_template.py'

        with open(path, 'r', encoding='utf-8') as f:
            output = f.read() + '\n'
            f.close()

        services = list(map(self.__serviceGenerator.generate, definitions))

        output += '\n'.join(services)

        tag2Services = self.__tags2ServicesPreparer.prepare(definitions)

        output += (
            '\n'
            '    def __generateTags2Services(self):\n'
            '        return ' + json.dumps(tag2Services) + '\n'
        )

        return output
