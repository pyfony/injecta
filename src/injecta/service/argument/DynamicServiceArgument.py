from injecta.generator.ServiceMethodNameTranslator import ServiceMethodNameTranslator
from injecta.service.argument.ArgumentInterface import ArgumentInterface
from injecta.service.class_.InspectedArgument import InspectedArgument

class DynamicServiceArgument(ArgumentInterface):

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
        return 'self.getByIdent(self.__parameters.' + self.__serviceName[1:-1] + '[1:])'

    def checkTypeMatchesDefinition(self, inspectedArgument: InspectedArgument, services2Classes: dict):
        # Note: Checking type of DynamicServiceArgument the same way as in ServiceArgument would require much more effort.
        return

    def __eq__(self, other: 'DynamicServiceArgument'):
        return self.name == other.name and self.getStringValue() == other.getStringValue()
