from Injecta.Argument.ArgumentInterface import ArgumentInterface

# see https://github.com/symfony/dependency-injection/blob/master/Definition.php
class Definition:

    def __init__(self, name: str, classFqn: str, arguments: list = [], tags: list = []):
        self.__name = name
        self.__classFqn = classFqn
        self.__arguments = arguments or []
        self.__import = 'from ' + classFqn + ' import ' + self.getClassName()
        self.__autowire = True
        self.__tags = tags or []
        self.__factoryService = None
        self.__factoryMethod = None

    def getName(self):
        return self.__name

    def getClassName(self):
        return self.__classFqn[self.__classFqn.rfind('.') + 1:]

    def getClassFqn(self):
        return self.__classFqn

    def setImport(self, importString):
        self.__import = importString

    def getImport(self):
        return self.__import

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
