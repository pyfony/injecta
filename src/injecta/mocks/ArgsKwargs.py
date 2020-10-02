class ArgsKwargs:

    def __init__(self, name: str, *args, **kwargs):
        self.__name = name
        self.__args = args
        self.__age = kwargs.get('age')
