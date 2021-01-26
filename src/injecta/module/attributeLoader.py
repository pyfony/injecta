from importlib import import_module

def load(moduleName, attributeName):
    try:
        module = import_module(moduleName)
    except ModuleNotFoundError:
        raise Exception(f'No module named {moduleName} (attribute: {attributeName})')

    return getattr(module, attributeName)

def loadFromString(val):
    moduleName, classAndMethod = val.split(':')

    if '.' not in classAndMethod:
        return load(moduleName, classAndMethod)

    className, methodName = classAndMethod.split('.')

    class_ = load(moduleName, className) # pylint: disable = invalid-name

    return getattr(class_, methodName)
