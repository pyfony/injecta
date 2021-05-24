from typing import Union


def get(object_or_class: Union[object, type]):
    if isinstance(object_or_class, type):
        module = object_or_class.__module__
        class_name = object_or_class.__name__
    else:
        class_ = object_or_class.__class__
        module = class_.__module__
        class_name = class_.__name__

    if module == "builtins":
        return class_name  # avoid outputs like 'builtins.str'

    return module + "." + class_name
