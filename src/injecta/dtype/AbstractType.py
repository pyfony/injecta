from abc import ABC

class AbstractType(ABC):

    def __init__(self, moduleName: str, className: str):
        self._moduleName = moduleName
        self._className = className

    @property
    def moduleName(self):
        return self._moduleName

    @property
    def className(self):
        return self._className

    def isPrimitiveType(self) -> bool:
        return self._moduleName == 'builtins'

    def isDefined(self) -> bool:
        return self._moduleName != 'inspect' and self._className != '_empty'

    def __str__(self):
        return self._moduleName + '.' + self._className
