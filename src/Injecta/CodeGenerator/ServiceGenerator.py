from Injecta.Definition import Definition
from Injecta.CodeGenerator.ObjectGenerator import ObjectGenerator
from Injecta.CodeGenerator.ServiceMethodNameTranslator import ServiceMethodNameTranslator

class ServiceGenerator:

    def __init__(
        self,
        objectGenerator: ObjectGenerator,
        serviceMethodNameTranslator: ServiceMethodNameTranslator
        ):
        self.__objectGenerator = objectGenerator
        self.__serviceMethodNameTranslator = serviceMethodNameTranslator
        
    def generate(self, definition: Definition):
        methodName = self.__serviceMethodNameTranslator.translate(definition.getName())

        service = (
            '    @DIService\n'
            '    def ' + methodName + '(self):\n'
            '' + self.__objectGenerator.generate(definition) + '\n'
        )

        return service
