from Injecta.Argument.ArgumentInterface import ArgumentInterface
import re

class ValueArgument(ArgumentInterface):

    def __init__(self, value):
        self.__value = value

    def getValue(self):
        if isinstance(self.__value, str):
            return self.__getStringValue()

        if isinstance(self.__value, bool):
            return 'True' if self.__value is True else 'False'

        return self.__value

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
