class ParameterArgument:

    def __init__(self, name: str):
        self.__name = name

    def getValue(self):
        return 'self.__config.' + self.__name
