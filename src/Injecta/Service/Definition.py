from Injecta.Argument.ArgumentInterface import ArgumentInterface
from Injecta.Module.ModuleClass import ModuleClass

# see https://github.com/symfony/dependency-injection/blob/master/Definition.php
class Definition:

    def __init__(self, name: str, moduleClass: ModuleClass, arguments: list = None, tags: list = None):
        self.__name = name
        self.__moduleClass = moduleClass
        self.__arguments = arguments or []
        self.__autowire = True
        self.__tags = tags or []
        self.__factoryService = None
        self.__factoryMethod = None

    def getName(self):
        return self.__name

    def getModuleClass(self) -> ModuleClass:
        return self.__moduleClass

    def hasArguments(self):
        return self.__arguments != []

    def getArguments(self):
        return self.__arguments

    def setAutowire(self, autowire: bool):
        self.__autowire = autowire

    def getAutowire(self) -> bool:
        return self.__autowire

    def getTags(self):
        return self.__tags

    def hasTags(self):
        return self.__tags != []

    def setFactory(self, factoryService: ArgumentInterface, factoryMethod: str):
        self.__factoryService = factoryService
        self.__factoryMethod = factoryMethod
        self.__autowire = False

    def getFactoryService(self) -> ArgumentInterface:
        return self.__factoryService

    def getFactoryMethod(self) -> str:
        return self.__factoryMethod
