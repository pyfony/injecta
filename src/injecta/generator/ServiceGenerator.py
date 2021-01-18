from injecta.generator.ObjectGenerator import ObjectGenerator
from injecta.generator.ServiceMethodNameTranslator import ServiceMethodNameTranslator
from injecta.service.resolved.ResolvedService import ResolvedService

class ServiceGenerator:

    def __init__(
        self,
        objectGenerator: ObjectGenerator,
        serviceMethodNameTranslator: ServiceMethodNameTranslator
    ):
        self.__objectGenerator = objectGenerator
        self.__serviceMethodNameTranslator = serviceMethodNameTranslator

    def generate(self, resolvedService: ResolvedService):
        methodName = self.__serviceMethodNameTranslator.translate(resolvedService.service.name)

        return (
            '    @diService\n'
            '    def ' + methodName + '(self):\n'
            '' + self.__objectGenerator.generate(resolvedService) + '\n'
        )

    def generateAliases(self, alias: str, serviceName: str):
        methodName = self.__serviceMethodNameTranslator.translate(alias)
        aliasMethodName = self.__serviceMethodNameTranslator.translate(serviceName)

        return (
            '    @diService\n'
            '    def ' + methodName + '(self):\n'
            '        return self.' + aliasMethodName + '()\n'
        )
