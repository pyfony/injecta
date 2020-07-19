from typing import List
from inspect import signature as createInspectSignature
from injecta.dtype.classLoader import loadClass
from injecta.dtype.DType import DType
from injecta.service.class_.InspectedArgument import InspectedArgument
from injecta.service.class_.InspectedArgumentResolver import InspectedArgumentResolver

class InspectedArgumentsResolver:

    def __init__(self):
        self.__inspectedArgumentResolver = InspectedArgumentResolver()

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

        return list(map(lambda argument: self.__inspectedArgumentResolver.resolve(argument[0], argument[1]), inspectedArguments))
