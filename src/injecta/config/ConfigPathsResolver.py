from typing import List, Dict
from injecta.config.ConfigLoader import ConfigLoader
from injecta.config.ImportDefinitionResolver import ImportDefinitionResolver
from pathlib import Path


class ConfigPathsResolver:
    def __init__(self):
        self.__config_loader = ConfigLoader()
        self.__import_definition_resolver = ImportDefinitionResolver()

    def resolve(self, config_path: Path, base_dir: Path, level=1) -> List[Dict]:
        yaml_config = self.__config_loader.load(config_path)
        config_paths = [{"path": config_path, "level": level}]

        if yaml_config is None:
            return []

        if "imports" in yaml_config:
            new_config_paths = []

            for import_definition in yaml_config["imports"]:
                new_config_paths += self.__import_definition_resolver.resolve(import_definition, base_dir)

            for new_config_path in new_config_paths:
                config_paths += self.resolve(new_config_path, base_dir, level + 1)

        return config_paths
