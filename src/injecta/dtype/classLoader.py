from importlib import import_module

def loadClass(moduleName, className):
    module = import_module(moduleName)
    return getattr(module, className)
