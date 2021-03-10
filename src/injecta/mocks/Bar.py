from injecta.mocks.BarInterface import BarInterface


class Bar(BarInterface):
    def __init__(self, name: str, number_with_default: int = 0, bool_with_default: bool = False):
        self.__name = name
        self.__number_with_default = number_with_default
        self.__bool_with_default = bool_with_default
