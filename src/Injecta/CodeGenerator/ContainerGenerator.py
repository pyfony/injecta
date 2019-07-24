import json
from Injecta.CodeGenerator.ServiceGenerator import ServiceGenerator
from Injecta.CodeGenerator.Tags2ServicesPreparer import Tags2ServicesPreparer
from Injecta.getLibRoot import getLibRoot

class ContainerGenerator:

    def __init__(self,
        serviceGenerator: ServiceGenerator,
        tags2ServicesPreparer: Tags2ServicesPreparer
    ):
        self.__serviceGenerator = serviceGenerator
        self.__tags2ServicesPreparer = tags2ServicesPreparer
        
    def generate(self, definitions: list):
        path = getLibRoot() + '/CodeGenerator/container_template.py'

        with open(path, 'r', encoding='utf-8') as f:
            output = f.read() + '\n'
            f.close()

        services = list(map(lambda x: self.__serviceGenerator.generate(x), definitions))

        output += '\n'.join(services)

        tag2Services = self.__tags2ServicesPreparer.prepare(definitions)

        output += (
            '\n'
            '    def __generateTags2Services(self):\n'
            '        return ' + json.dumps(tag2Services) + '\n'
        )

        return output
