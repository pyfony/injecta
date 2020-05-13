class Kwargs:

    def __init__(self, name: str, **kwargs):
        self.__name = name
        self.__age = kwargs.get('age')
