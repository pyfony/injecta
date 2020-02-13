import importlib.util

def resolvePath(rootModuleName: str):
    baseModuleSpec = importlib.util.find_spec(rootModuleName)

    if not baseModuleSpec:
        raise Exception('Cannot resolve root module {}'.format(rootModuleName))

    if baseModuleSpec.origin is not None:
        return baseModuleSpec.origin

    return baseModuleSpec.submodule_search_locations._path[0]  # pylint: disable = protected-access
