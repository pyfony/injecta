from injecta.definition.Definition import Definition
from injecta.generator.ObjectGenerator import ObjectGenerator
from injecta.generator.ServiceMethodNameTranslator import ServiceMethodNameTranslator

class ServiceGenerator:

    def __init__(
        self,
        objectGenerator: ObjectGenerator,
        serviceMethodNameTranslator: ServiceMethodNameTranslator
    ):
        self.__objectGenerator = objectGenerator
        self.__serviceMethodNameTranslator = serviceMethodNameTranslator

    def generate(self, definition: Definition):
        methodName = self.__serviceMethodNameTranslator.translate(definition.name)

        serviceMethodCode = (
            '    @diService\n'
            '    def ' + methodName + '(self):\n'
            '' + self.__objectGenerator.generate(definition) + '\n'
        )

        return serviceMethodCode
