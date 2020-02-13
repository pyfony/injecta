from typing import List
from injecta.generator.ServiceGenerator import ServiceGenerator
from injecta.service.Service import Service
from injecta.libRoot import getLibRoot

class ContainerGenerator:

    def __init__(self,
        serviceGenerator: ServiceGenerator,
    ):
        self.__serviceGenerator = serviceGenerator

    def generate(self, services: List[Service]):
        path = getLibRoot() + '/generator/container_template.py'

        with open(path, 'r', encoding='utf-8') as f:
            output = f.read() + '\n'
            f.close()

        codeOfServiceMethods = list(map(self.__serviceGenerator.generate, services))

        output += '\n'.join(codeOfServiceMethods)

        return output
