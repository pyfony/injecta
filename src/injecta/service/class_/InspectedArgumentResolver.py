from pydoc import locate
from inspect import Parameter, isclass
from injecta.dtype.ListType import ListType
from injecta.dtype.DType import DType
from injecta.service.class_.InspectedArgument import InspectedArgument


class InspectedArgumentResolver:
    def resolve(self, name: str, parameter: Parameter) -> InspectedArgument:
        annotation = parameter.annotation

        if annotation.__module__ == "typing":
            subtype_arg = annotation.__args__[0]

            dtype = ListType(subtype_arg.__module__, subtype_arg.__name__)

            inspected_argument = InspectedArgument(name, dtype)
        else:
            dtype = DType(annotation.__module__, annotation.__name__)

            default_value = parameter.default if not isinstance(parameter.default, locate("type")) else None
            default_value_set = not (
                parameter.default
                and isclass(parameter.default)
                and parameter.default.__module__ == "inspect"
                and parameter.default.__name__ == "_empty"
            )

            inspected_argument = InspectedArgument(name, dtype, default_value, default_value_set)

        return inspected_argument
