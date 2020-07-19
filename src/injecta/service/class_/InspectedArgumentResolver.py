from pydoc import locate
from inspect import Parameter, isclass
from injecta.dtype.ListType import ListType
from injecta.dtype.DType import DType
from injecta.service.class_.InspectedArgument import InspectedArgument

class InspectedArgumentResolver:

    def resolve(self, name: str, parameter: Parameter) -> InspectedArgument:
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
