import os
from pathlib import Path
from Injecta.Definition import Definition
from Injecta.CodeGenerator.ServiceGenerator import ServiceGenerator

class ContainerGenerator:

    def __init__(self,
        serviceGenerator: ServiceGenerator
    ):
        self.__serviceGenerator = serviceGenerator
        
    def generate(self, definitions: list):
        path = os.path.dirname(os.path.abspath(__file__)) + '/container_template.py'

        with open(path, 'r', encoding='utf-8') as f:
            output = f.read() + '\n'
            f.close()

        services = list(map(lambda x: self.__serviceGenerator.generate(x), definitions))

        output += '\n'.join(services)

        return output
