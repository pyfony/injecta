from pathlib import Path
from typing import Dict, List
from injecta.config.ConfigPathsResolver import ConfigPathsResolver
from injecta.config.ConfigLoaderAndMerger import ConfigLoaderAndMerger
from injecta.config.ConfigReaderInterface import ConfigReaderInterface


class YamlConfigReader(ConfigReaderInterface):
    def __init__(self):
        self.__config_paths_resolver = ConfigPathsResolver()
        self.__config_loader_and_merger = ConfigLoaderAndMerger()

    def read(self, config_path: str):
        resolved_paths = self.__config_paths_resolver.resolve(Path(config_path), Path(config_path).parent)
        resolved_paths_by_levels = self.__to_list_by_levels(resolved_paths)
        resolved_paths_by_levels.reverse()
        flattened_paths = [item for sublist in resolved_paths_by_levels for item in sublist]

        return self.__config_loader_and_merger.load_and_merge(flattened_paths)

    def __to_list_by_levels(self, resolved_paths: List[Dict]):
        config_paths_by_levels = dict()

        for resolved_path in resolved_paths:
            if resolved_path["level"] not in config_paths_by_levels:
                config_paths_by_levels[resolved_path["level"]] = []

            config_paths_by_levels[resolved_path["level"]].append(resolved_path["path"])

        return list(config_paths_by_levels.values())
