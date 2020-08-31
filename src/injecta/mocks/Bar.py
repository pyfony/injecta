from injecta.mocks.BarInterface import BarInterface

class Bar(BarInterface):

    def __init__(self, name: str, numberWithDefault: int = 0, boolWithDefault: bool = False):
        self.__name = name
        self.__numberWithDefault = numberWithDefault
        self.__boolWithDefault = boolWithDefault
