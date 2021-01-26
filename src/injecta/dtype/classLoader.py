from injecta.module import attributeLoader

# deprecated, use loadAttribute instead
def loadClass(moduleName, className):
    return attributeLoader.load(moduleName, className)
