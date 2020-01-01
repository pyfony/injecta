from injecta.dtype.AbstractType import AbstractType

class DType(AbstractType):

    def __eq__(self, other: 'DType'):
        return (
            self.moduleName == other.moduleName
            and self.className == other.className
        )
