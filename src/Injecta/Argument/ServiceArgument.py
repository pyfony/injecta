from Injecta.Argument.ArgumentInterface import ArgumentInterface

class ServiceArgument(ArgumentInterface):

    def __init__(self, name: str):
        self.__name = name

    def getValue(self):
        return 'self.__' + self.__name[0].upper() + self.__name[1:].replace('.', '_') + '()'
