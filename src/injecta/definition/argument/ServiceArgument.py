from injecta.generator.ServiceMethodNameTranslator import ServiceMethodNameTranslator
from injecta.definition.argument.ArgumentInterface import ArgumentInterface
from injecta.service.ServiceValidatorException import ServiceValidatorException
from injecta.service.class_.ConstructorArgument import ConstructorArgument
from injecta.dtype.DType import DType
from injecta.dtype.classLoader import loadClass

class ServiceArgument(ArgumentInterface):

    __serviceMethodTranslator = ServiceMethodNameTranslator()

    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def getStringValue(self):
        return 'self.' + self.__serviceMethodTranslator.translate(self.__name) + '()'

    def checkTypeMatchesDefinition(self, constructorArgument: ConstructorArgument, services2Classes: dict):
        serviceClassType = services2Classes[self.__name] # type: DType

        if serviceClassType == constructorArgument.dtype:
            return

        serviceClass = loadClass(serviceClassType.moduleName, serviceClassType.className)
        constructorArgumentClass = loadClass(constructorArgument.dtype.moduleName, constructorArgument.dtype.className)

        if not issubclass(serviceClass, constructorArgumentClass):
            raise ServiceValidatorException(constructorArgument.name, str(constructorArgument.dtype), str(serviceClassType))

    def __eq__(self, other: 'ServiceArgument'):
        return self.getStringValue() == other.getStringValue()
