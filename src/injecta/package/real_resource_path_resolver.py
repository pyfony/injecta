from pathlib import Path
from injecta.package.path_resolver import resolve_path


def resolve_real_resource_path(package_resource_path: str) -> Path:
    if package_resource_path[0:1] != "@":
        raise Exception("Package resource path must start with @[packageName]")

    first_slash_position = package_resource_path.find("/")
    root_module_name = package_resource_path[1:first_slash_position]
    root_module_path = resolve_path(root_module_name)

    return Path(root_module_path + package_resource_path[first_slash_position:])
