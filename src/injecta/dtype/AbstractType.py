from abc import ABC


class AbstractType(ABC):
    def __init__(self, module_name: str, class_name: str):
        self._module_name = module_name
        self._class_name = class_name

    @property
    def module_name(self):
        return self._module_name

    @property
    def class_name(self):
        return self._class_name

    def is_primitive_type(self) -> bool:
        return self._module_name == "builtins"

    def is_defined(self) -> bool:
        return self._module_name != "inspect" and self._class_name != "_empty"

    def __str__(self):
        return self._module_name + "." + self._class_name
