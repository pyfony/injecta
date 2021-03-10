from pathlib import Path
from injecta.package.real_resource_path_resolver import resolve_real_resource_path


class ImportDefinitionResolver:
    def resolve(self, import_definition, base_dir: Path) -> set:
        if isinstance(import_definition, str):
            if import_definition[0:1] == "@":
                return {resolve_real_resource_path(import_definition)}

            return {base_dir.joinpath(import_definition).resolve()}

        if isinstance(import_definition, dict):
            if "search" not in import_definition:
                raise Exception('Missing the "search" main keyword in the import definition')

            if "include" not in import_definition["search"]:
                raise Exception('Missing the "include" keyword under "search" main keyword')

            base_path_glob = set(base_dir.glob("./**/*.*"))
            all_configs_glob = set(map(lambda path: path.resolve(), base_dir.glob(import_definition["search"]["include"])))

            return set(all_configs_glob - base_path_glob)

        raise Exception("Unexpected import definition type: " + type(import_definition))
