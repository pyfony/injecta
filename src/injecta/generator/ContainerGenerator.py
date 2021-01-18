from typing import List
from injecta.generator.ServiceGenerator import ServiceGenerator
from injecta.libRoot import getLibRoot
from injecta.service.resolved.ResolvedService import ResolvedService

class ContainerGenerator:

    def __init__(self,
        serviceGenerator: ServiceGenerator,
    ):
        self.__serviceGenerator = serviceGenerator

    def generate(self, resolvedServices: List[ResolvedService], aliases2Services: dict):
        path = getLibRoot() + '/generator/container_template.py'

        with open(path, 'r', encoding='utf-8') as f:
            output = f.read() + '\n'
            f.close()

        codeOfServiceMethods = list(map(self.__serviceGenerator.generate, resolvedServices))
        codeOfServiceAliasMethods = [self.__serviceGenerator.generateAliases(alias, serviceName) for alias, serviceName in aliases2Services.items()]

        output += '\n'.join(codeOfServiceMethods + codeOfServiceAliasMethods)

        return output
