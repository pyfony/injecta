from injecta.dtype.AbstractType import AbstractType


class ListType(AbstractType):
    def __eq__(self, other: "ListType"):
        return self.module_name == other.module_name and self.class_name == other.class_name
