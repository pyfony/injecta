from os import path
from injecta.dtype.DType import DType
from injecta.package.path_resolver import resolve_path


class DTypeResolver:
    def resolve(self, dtype_str: str) -> DType:
        last_dot_index = dtype_str.rfind(".")

        class_name = dtype_str[last_dot_index + 1 :]  # noqa: 5203
        root_module_name = dtype_str[: dtype_str.find(".")]

        root_module_path = resolve_path(root_module_name)

        file_path = root_module_path[: -len(root_module_name)] + dtype_str.replace(".", "/") + ".py"

        if path.exists(file_path):
            # from foo.bar.HelloClass import HelloClass
            module_name = dtype_str
        else:
            # from foo.bar import HelloClass
            module_name = dtype_str[:last_dot_index]

        return DType(module_name, class_name)
