import re
from injecta.service.argument.ArgumentInterface import ArgumentInterface
from injecta.service.ServiceValidatorException import ServiceValidatorException
from injecta.service.class_.InspectedArgument import InspectedArgument

class PrimitiveArgument(ArgumentInterface):

    def __init__(self, value, name: str = None):
        self.__value = value
        self.__name = name

    @property
    def name(self):
        return self.__name

    def getStringValue(self):
        if isinstance(self.__value, str):
            return self.__getStringValue()

        if isinstance(self.__value, bool):
            return 'True' if self.__value is True else 'False'

        return str(self.__value)

    def checkTypeMatchesDefinition(self, inspectedArgument: InspectedArgument, services2Classes: dict):
        dtype = inspectedArgument.dtype

        if dtype.moduleName == 'box':
            return

        if dtype.isPrimitiveType() is False:
            raise ServiceValidatorException(
                inspectedArgument.name,
                str(inspectedArgument.dtype),
                self.__value.__class__.__name__
            )

    def __getStringValue(self):
        output = self.__value

        if re.match(r'^%env\(([^)]+)\)%$', output):
            return re.sub(r'^%env\(([^)]+)\)%$', 'os.environ[\'\\g<1>\']', output)

        if re.match(r'^%([^%]+)%$', output):
            return re.sub(r'^%([^%]+)%$', 'self.__parameters.\\g<1>', output)

        output = re.sub(r'%env\(([^)]+)\)%', '\' + os.environ[\'\\g<1>\'] + \'', output)
        output = re.sub(r'%([^%]+)%', '\' + self.__parameters.\\g<1> + \'', output)

        output = '\'' + output + '\''

        output = re.sub(r' \+ \'\'$', '', output)
        output = re.sub(r'^\'\' \+ ', '', output)

        return output

    def __eq__(self, other: 'PrimitiveArgument'):
        return self.name == other.name and self.getStringValue() == other.getStringValue()
