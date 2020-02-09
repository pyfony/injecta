import re
from injecta.definition.argument.ArgumentInterface import ArgumentInterface
from injecta.service.ServiceValidatorException import ServiceValidatorException
from injecta.service.class_.ConstructorArgument import ConstructorArgument

class PrimitiveArgument(ArgumentInterface):

    def __init__(self, value):
        self.__value = value

    def getStringValue(self):
        if isinstance(self.__value, str):
            return self.__getStringValue()

        if isinstance(self.__value, bool):
            return 'True' if self.__value is True else 'False'

        return str(self.__value)

    def checkTypeMatchesDefinition(self, constructorArgument: ConstructorArgument, services2Classes: dict):
        dtype = constructorArgument.dtype

        if dtype.moduleName == 'box':
            return

        if dtype.isPrimitiveType() is False:
            raise ServiceValidatorException(
                constructorArgument.name,
                str(constructorArgument.dtype),
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
        return self.getStringValue() == other.getStringValue()
