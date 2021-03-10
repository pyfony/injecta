from injecta.module import attribute_loader

# deprecated, use loadAttribute instead
def load_class(module_name, class_name):  # noqa: 5302
    return attribute_loader.load(module_name, class_name)
