from os import path
from injecta.dtype.DType import DType
import importlib.util

class DTypeResolver:

    def resolve(self, dtypeStr: str) -> DType:
        lastDotIndex = dtypeStr.rfind('.')

        className = dtypeStr[lastDotIndex + 1:]
        rootModuleName = dtypeStr[:dtypeStr.find('.')]

        baseModuleSpec = importlib.util.find_spec(rootModuleName)

        if not baseModuleSpec:
            raise Exception('Cannot resolve root module {}'.format(rootModuleName))

        if baseModuleSpec.origin is not None:
            rootModulePath = baseModuleSpec.origin
        else:
            rootModulePath = baseModuleSpec.submodule_search_locations._path[0] # pylint: disable = protected-access

        filePath = rootModulePath[:-len(rootModuleName)] + dtypeStr.replace('.', '/') + '.py'

        if path.exists(filePath):
            # from foo.bar.HelloClass import HelloClass
            moduleName = dtypeStr
        else:
            # from foo.bar import HelloClass
            moduleName = dtypeStr[:lastDotIndex]

        return DType(moduleName, className)
