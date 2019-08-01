from Injecta.Module.ModuleClass import ModuleClass
import importlib

class ModuleClassResolver:

    def resolve(self, classFqn: str) -> ModuleClass:
        className = classFqn[classFqn.rfind('.') + 1:]

        try:
            # from Foo.Bar.HelloClass import HelloClass
            module = importlib.import_module(classFqn)
        except ImportError:
            # from foo.bar import HelloClass
            standardModuleName = classFqn[:classFqn.rfind('.')]
            module = importlib.import_module(standardModuleName)

        return ModuleClass(module, className)
