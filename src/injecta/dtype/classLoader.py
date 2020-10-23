from importlib import import_module

def loadClass(moduleName, className):
    try:
        module = import_module(moduleName)
    except ModuleNotFoundError:
        raise Exception(f'No module named {moduleName} (class {className})')

    return getattr(module, className)
