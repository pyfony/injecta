from importlib import import_module


def load(module_name, attribute_name):
    try:
        module = import_module(module_name)
    except ModuleNotFoundError:
        raise Exception(f"No module named {module_name} (attribute: {attribute_name})")

    return getattr(module, attribute_name)


def load_from_string(val):
    module_name, class_and_method = val.split(":")

    if "." not in class_and_method:
        return load(module_name, class_and_method)

    class_name, method_name = class_and_method.split(".")

    class_ = load(module_name, class_name)

    return getattr(class_, method_name)
