from injecta.dtype.AbstractType import AbstractType

class ListType(AbstractType):

    def __eq__(self, other: 'ListType'):
        return (
            self.moduleName == other.moduleName
            and self.className == other.className
        )
