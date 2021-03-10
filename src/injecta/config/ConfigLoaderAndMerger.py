from pathlib import Path
from typing import List
from injecta.config.ConfigLoader import ConfigLoader
from injecta.config.ConfigMerger import ConfigMerger


class ConfigLoaderAndMerger:
    def __init__(self):
        self.__config_loader = ConfigLoader()
        self.__config_merger = ConfigMerger()

    def load_and_merge(self, config_paths: List[Path]):
        yaml_config = {}

        for config_path in config_paths:
            new_yaml_config = self.__config_loader.load(config_path)

            if "imports" in new_yaml_config:
                del new_yaml_config["imports"]

            yaml_config = self.__config_merger.merge(yaml_config, new_yaml_config)

        return yaml_config
