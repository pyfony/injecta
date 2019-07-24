from Injecta.Argument.ArgumentInterface import ArgumentInterface

class ValueArgument(ArgumentInterface):

    def __init__(self, value: str):
        self.__value = value

    def getValue(self):
        if isinstance(self.__value, str):
            return '\'' + self.__value + '\''
        if isinstance(self.__value, bool):
            return 'True' if self.__value is True else 'False'
        else:
            return self.__value
