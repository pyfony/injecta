from typing import List
from injecta.dtype.DType import DType
from injecta.service.argument.ArgumentInterface import ArgumentInterface
from injecta.service.argument.ServiceArgument import ServiceArgument

class Service:

    def __init__(self, name: str, class_: DType, arguments: List[ArgumentInterface] = None, tags: list = None):
        self.__name = name
        self.__class = class_
        self.__arguments = arguments or []
        self.__autowire = True
        self.__tags = tags or []
        self.__factoryService = None
        self.__factoryMethod = None

    @property
    def name(self) -> str:
        return self.__name

    @property
    def class_(self) -> DType: # pylint: disable = invalid-name
        return self.__class

    @property
    def arguments(self) -> List[ArgumentInterface]:
        return self.__arguments

    def hasNamedArguments(self) -> bool:
        for argument in self.__arguments:
            if argument.name is not None:
                return True

        return False

    def setAutowire(self, autowire: bool):
        self.__autowire = autowire

    @property
    def autowire(self) -> bool:
        return self.__autowire

    @property
    def tags(self) -> list:
        return self.__tags

    def getTagAttributes(self, tagName: str):
        for tag in self.__tags:
            if isinstance(tag, dict) and tag['name'] == tagName:
                return tag

        raise Exception(f'No attributes found for tag {tagName}')

    def setFactory(self, factoryService: ServiceArgument, factoryMethod: str):
        self.__factoryService = factoryService
        self.__factoryMethod = factoryMethod
        self.__autowire = False

    @property
    def factoryService(self) -> ServiceArgument:
        return self.__factoryService

    @property
    def factoryMethod(self) -> str:
        return self.__factoryMethod

    def usesFactory(self) -> bool:
        return self.__factoryMethod is not None

    def __eq__(self, other: 'Service'):
        return (
            self.name == other.name
            and self.class_ == other.class_
            and self.arguments == other.arguments
            and self.autowire == other.autowire
            and self.tags == other.tags
            and self.factoryService == other.factoryService
            and self.factoryMethod == other.factoryMethod
        )
