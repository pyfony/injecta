from injecta.dtype.AbstractType import AbstractType

class InspectedArgument:

    def __init__(
        self,
        name: str,
        dtype: AbstractType,
        defaultValue=None,
        defaultValueSet=False,
    ):
        self.__name = name
        self.__dtype = dtype
        self.__defaultValue = defaultValue
        self.__defaultValueSet = defaultValueSet

    @property
    def name(self) -> str:
        return self.__name

    @property
    def dtype(self) -> AbstractType:
        return self.__dtype

    @property
    def defaultValue(self):
        return self.__defaultValue

    def hasDefaultValue(self):
        return self.__defaultValueSet

    def __eq__(self, other: 'InspectedArgument'):
        return (
            self.name == other.name
            and self.dtype == other.dtype
            and self.defaultValue == other.defaultValue
        )
