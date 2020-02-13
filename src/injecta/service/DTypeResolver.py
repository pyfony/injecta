from os import path
from injecta.dtype.DType import DType
from injecta.package.pathResolver import resolvePath

class DTypeResolver:

    def resolve(self, dtypeStr: str) -> DType:
        lastDotIndex = dtypeStr.rfind('.')

        className = dtypeStr[lastDotIndex + 1:]
        rootModuleName = dtypeStr[:dtypeStr.find('.')]

        rootModulePath = resolvePath(rootModuleName)

        filePath = rootModulePath[:-len(rootModuleName)] + dtypeStr.replace('.', '/') + '.py'

        if path.exists(filePath):
            # from foo.bar.HelloClass import HelloClass
            moduleName = dtypeStr
        else:
            # from foo.bar import HelloClass
            moduleName = dtypeStr[:lastDotIndex]

        return DType(moduleName, className)
