from injecta.dtype.AbstractType import AbstractType

class ConstructorArgument:

    def __init__(
        self,
        name: str,
        dtype: AbstractType,
        defaultValue=None,
    ):
        self.__name = name
        self.__dtype = dtype
        self.__defaultValue = defaultValue

    @property
    def name(self) -> str:
        return self.__name

    @property
    def dtype(self) -> AbstractType:
        return self.__dtype

    @property
    def defaultValue(self):
        return self.__defaultValue

    def __eq__(self, other: 'ConstructorArgument'):
        return (
                self.name == other.name
                and self.dtype == other.dtype
                and self.defaultValue == other.defaultValue
        )
