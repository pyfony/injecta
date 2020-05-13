from pydoc import locate
from typing import List
from inspect import signature as createInspectSignature
from inspect import Parameter
from injecta.dtype.ListType import ListType
from injecta.dtype.classLoader import loadClass
from injecta.dtype.DType import DType
from injecta.service.class_.InspectedArgument import InspectedArgument

class InspectedArgumentsResolver:

    def resolve(self, dtype: DType) -> List[InspectedArgument]:
        classDefinition = loadClass(dtype.moduleName, dtype.className)

        # constructor is missing
        if '__init__' not in classDefinition.__dict__:
            return []

        signature = createInspectSignature(classDefinition.__init__)

        def isConstructorArgument(argument):
            argumentName, _ = argument
            return argumentName != 'self'

        inspectedArguments = list(filter(isConstructorArgument, signature.parameters.items()))

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

            inspectedArgument = InspectedArgument(name, dtype, defaultValue)

        return inspectedArgument
