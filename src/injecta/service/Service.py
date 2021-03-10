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
        self.__factory_service = None
        self.__factory_method = None

    @property
    def name(self) -> str:
        return self.__name

    @property
    def class_(self) -> DType:
        return self.__class

    @property
    def arguments(self) -> List[ArgumentInterface]:
        return self.__arguments

    def has_named_arguments(self) -> bool:
        for argument in self.__arguments:
            if argument.name is not None:
                return True

        return False

    def set_autowire(self, autowire: bool):
        self.__autowire = autowire

    @property
    def autowire(self) -> bool:
        return self.__autowire

    @property
    def tags(self) -> list:
        return self.__tags

    def get_tag_attributes(self, tag_name: str):
        for tag in self.__tags:
            if isinstance(tag, dict) and tag["name"] == tag_name:
                return tag

        raise Exception(f"No attributes found for tag {tag_name}")

    def set_factory(self, factory_service: ServiceArgument, factory_method: str):
        self.__factory_service = factory_service
        self.__factory_method = factory_method
        self.__autowire = False

    @property
    def factory_service(self) -> ServiceArgument:
        return self.__factory_service

    @property
    def factory_method(self) -> str:
        return self.__factory_method

    def uses_factory(self) -> bool:
        return self.__factory_method is not None

    def __eq__(self, other: "Service"):
        return (
            self.name == other.name
            and self.class_ == other.class_
            and self.arguments == other.arguments
            and self.autowire == other.autowire
            and self.tags == other.tags
            and self.factory_service == other.factory_service
            and self.factory_method == other.factory_method
        )
