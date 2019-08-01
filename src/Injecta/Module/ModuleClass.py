class ModuleClass:

    def __init__(self, module, className):
        self.__module = module
        self.__className = className

    def getModule(self):
        return self.__module

    def getModuleName(self):
        return self.__module.__name__

    def getClassName(self):
        return self.__className
