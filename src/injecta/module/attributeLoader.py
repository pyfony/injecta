from importlib import import_module

def load(moduleName, attributeName):
    try:
        module = import_module(moduleName)
    except ModuleNotFoundError:
        raise Exception(f'No module named {moduleName} (attribute: {attributeName})')

    return getattr(module, attributeName)
