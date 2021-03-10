from typing import List
from inspect import signature as create_inspect_signature
from injecta.dtype.DType import DType
from injecta.service.class_.InspectedArgument import InspectedArgument
from injecta.service.class_.InspectedArgumentResolver import InspectedArgumentResolver
from injecta.module import attribute_loader


class InspectedArgumentsResolver:
    def __init__(self):
        self.__inspected_argument_resolver = InspectedArgumentResolver()

    def resolve_constructor(self, dtype: DType) -> List[InspectedArgument]:
        class_definition = attribute_loader.load(dtype.module_name, dtype.class_name)

        while "__init__" not in class_definition.__dict__:
            first_parent_class = class_definition.__bases__[0]

            # no constructor found in base class or parents
            if first_parent_class.__module__ == "builtins" and first_parent_class.__name__ == "object":
                return []

            class_definition = attribute_loader.load(first_parent_class.__module__, first_parent_class.__name__)

        return self.__resolve(getattr(class_definition, "__init__"))

    def resolve_method(self, dtype: DType, method_name: str) -> List[InspectedArgument]:
        class_definition = attribute_loader.load(dtype.module_name, dtype.class_name)

        return self.__resolve(getattr(class_definition, method_name))

    def __resolve(self, obj):
        signature = create_inspect_signature(obj)

        def is_real_argument(argument):
            argument_name, _ = argument
            return argument_name != "self"

        inspected_arguments = list(filter(is_real_argument, signature.parameters.items()))

        return list(map(lambda argument: self.__inspected_argument_resolver.resolve(argument[0], argument[1]), inspected_arguments))
