from pydoc import locate
from typing import List
from inspect import signature as createInspectSignature
from inspect import Parameter, isclass
from injecta.dtype.ListType import ListType
from injecta.dtype.classLoader import loadClass
from injecta.dtype.DType import DType
from injecta.service.class_.InspectedArgument import InspectedArgument

class InspectedArgumentsResolver:

    def resolveConstructor(self, dtype: DType) -> List[InspectedArgument]:
        classDefinition = loadClass(dtype.moduleName, dtype.className)

        while '__init__' not in classDefinition.__dict__:
            firstParentClass = classDefinition.__bases__[0]

            # no constructor found in base class or parents
            if firstParentClass.__module__ == 'builtins' and firstParentClass.__name__ == 'object':
                return []

            classDefinition = loadClass(firstParentClass.__module__, firstParentClass.__name__)

        return self.__resolve(getattr(classDefinition, '__init__'))

    def resolveMethod(self, dtype: DType, methodName: str) -> List[InspectedArgument]:
        classDefinition = loadClass(dtype.moduleName, dtype.className)

        return self.__resolve(getattr(classDefinition, methodName))

    def __resolve(self, obj):
        signature = createInspectSignature(obj)

        def isRealArgument(argument):
            argumentName, _ = argument
            return argumentName != 'self'

        inspectedArguments = list(filter(isRealArgument, signature.parameters.items()))

        return list(map(lambda argument: self.__createArgument(argument[0], argument[1]), inspectedArguments))

    def __createArgument(self, name: str, parameter: Parameter) -> InspectedArgument:
        annotation = parameter.annotation

        if annotation.__module__ == 'typing':
            subtypeArg = annotation.__args__[0]

            dtype = ListType(subtypeArg.__module__, subtypeArg.__name__)

            inspectedArgument = InspectedArgument(name, dtype)
        else:
            dtype = DType(annotation.__module__, annotation.__name__)

            defaultValue = parameter.default if not isinstance(parameter.default, locate('type')) else None
            defaultValueSet = not (
                parameter.default
                and isclass(parameter.default)
                and parameter.default.__module__ == 'inspect'
                and parameter.default.__name__ == '_empty'
            )

            inspectedArgument = InspectedArgument(name, dtype, defaultValue, defaultValueSet)

        return inspectedArgument
