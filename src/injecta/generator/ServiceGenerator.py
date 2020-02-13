from injecta.service.Service import Service
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

    def generate(self, service: Service):
        methodName = self.__serviceMethodNameTranslator.translate(service.name)

        serviceMethodCode = (
            '    @diService\n'
            '    def ' + methodName + '(self):\n'
            '' + self.__objectGenerator.generate(service) + '\n'
        )

        return serviceMethodCode
