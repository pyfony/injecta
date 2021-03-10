from injecta.dtype.AbstractType import AbstractType


class InspectedArgument:
    def __init__(
        self,
        name: str,
        dtype: AbstractType,
        default_value=None,
        default_value_set=False,
    ):
        self.__name = name
        self.__dtype = dtype
        self.__default_value = default_value
        self.__default_value_set = default_value_set

    @property
    def name(self) -> str:
        return self.__name

    @property
    def dtype(self) -> AbstractType:
        return self.__dtype

    @property
    def default_value(self):
        return self.__default_value

    def has_default_value(self):
        return self.__default_value_set

    def __eq__(self, other: "InspectedArgument"):
        return self.name == other.name and self.dtype == other.dtype and self.default_value == other.default_value
