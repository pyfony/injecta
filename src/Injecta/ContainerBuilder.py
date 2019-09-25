from typing import List
from Injecta.Autowiring.Autowirer import Autowirer
from Injecta.Autowiring.ArgumentResolver import ArgumentResolver
from Injecta.CodeGenerator.ContainerGenerator import ContainerGenerator
from Injecta.CodeGenerator.ServiceGenerator import ServiceGenerator
from Injecta.CodeGenerator.ObjectGenerator import ObjectGenerator
from Injecta.CodeGenerator.Tags2ServicesPreparer import Tags2ServicesPreparer
from Injecta.ClassListBuilder import ClassListBuilder
from Injecta.CodeGenerator.ServiceMethodNameTranslator import ServiceMethodNameTranslator
from Injecta.Service.Definition import Definition

class ContainerBuilder:

    def __init__(self):
        self.__classListBuilder = ClassListBuilder()
        self.__autowirer = Autowirer(
            ArgumentResolver()
        )
        self.__containerGenerator = ContainerGenerator(
            ServiceGenerator(
                ObjectGenerator(),
                ServiceMethodNameTranslator()
            ),
            Tags2ServicesPreparer()
        )

    def build(self, definitions: List[Definition]):
        classes = self.__classListBuilder.buildClassList(definitions)

        definitions = list(map(lambda definition: self.__autowirer.autowire(definition, classes), definitions))

        return self.__containerGenerator.generate(definitions)
