from Injecta.Argument.ArgumentInterface import ArgumentInterface

class ParameterArgument(ArgumentInterface):

    def __init__(self, name: str):
        self.__name = name

    def getValue(self):
        if self.__name[:4] == 'env(':
            envVariableName = self.__name[4:-1]
            return 'os.environ[\'{}\']'.format(envVariableName)
        else:
            return 'self.__config.' + self.__name
