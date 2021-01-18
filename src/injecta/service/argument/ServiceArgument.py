from injecta.generator.ServiceMethodNameTranslator import ServiceMethodNameTranslator
from injecta.service.argument.ArgumentInterface import ArgumentInterface
from injecta.service.argument.validator.ArgumentsValidatorException import ArgumentsValidatorException
from injecta.service.class_.InspectedArgument import InspectedArgument
from injecta.dtype.DType import DType
from injecta.dtype.classLoader import loadClass

class ServiceArgument(ArgumentInterface):

    __serviceMethodTranslator = ServiceMethodNameTranslator()

    def __init__(self, serviceName: str, name: str = None):
        self.__serviceName = serviceName
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def serviceName(self):
        return self.__serviceName

    def getStringValue(self):
        return 'self.' + self.__serviceMethodTranslator.translate(self.__serviceName) + '()'

    def checkTypeMatchesDefinition(self, inspectedArgument: InspectedArgument, services2Classes: dict, aliases2Services: dict):
        serviceClassType = self.__resolveServiceClassType(services2Classes, aliases2Services)

        if serviceClassType == inspectedArgument.dtype:
            return

        serviceClass = loadClass(serviceClassType.moduleName, serviceClassType.className)
        inspectedArgumentClass = loadClass(inspectedArgument.dtype.moduleName, inspectedArgument.dtype.className)

        if not issubclass(serviceClass, inspectedArgumentClass):
            raise ArgumentsValidatorException(inspectedArgument.name, str(inspectedArgument.dtype), str(serviceClassType))

    def __resolveServiceClassType(self, services2Classes: dict, aliases2Services: dict) -> DType:
        if self.__serviceName in services2Classes:
            return services2Classes[self.__serviceName]

        if self.__serviceName in aliases2Services:
            def resolveRecursive(serviceName):
                aliasedServiceName = aliases2Services[serviceName]

                if aliasedServiceName in aliases2Services:
                    return resolveRecursive(aliasedServiceName)

                if aliasedServiceName not in services2Classes:
                    raise Exception(f'Aliased service "{aliasedServiceName}" does not exist')

                return services2Classes[aliasedServiceName]

            return resolveRecursive(self.__serviceName)

        raise Exception(f'Undefined service {self.__serviceName}')

    def __eq__(self, other: 'ServiceArgument'):
        return self.name == other.name and self.getStringValue() == other.getStringValue()
