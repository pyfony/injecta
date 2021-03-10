import importlib.util


def resolve_path(root_module_name: str):
    base_module_spec = importlib.util.find_spec(root_module_name)

    if not base_module_spec:
        raise Exception("Cannot resolve root module {}".format(root_module_name))

    if base_module_spec.origin is not None:
        return base_module_spec.origin

    return base_module_spec.submodule_search_locations._path[0]
