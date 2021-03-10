from injecta.dtype.AbstractType import AbstractType


class DType(AbstractType):
    def __eq__(self, other: "DType"):
        return self.module_name == other.module_name and self.class_name == other.class_name
