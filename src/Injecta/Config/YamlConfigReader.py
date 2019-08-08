from pathlib import Path
import yaml
from box import Box
from Injecta.Config.PlaceholderReplacer import PlaceholderReplacer

class YamlConfigReader:

    def __init__(self):
        self.__placeholderReplacer = PlaceholderReplacer()

    def read(self, parametersPaths):
        # for backward compatibility
        if isinstance(parametersPaths, str):
            parametersPaths = [parametersPaths]

        config = {}

        for parametersPath in parametersPaths:
            newConfig = self.__loadConfig(parametersPath)
            config = {**config, **newConfig}

        config = self.__placeholderReplacer.replace(config)

        return Box(config)

    def __loadConfig(self, parametersPath: str):
        if not Path(parametersPath).is_file():
            raise Exception('{} does not exist'.format(parametersPath))

        with open(parametersPath, 'r', encoding='utf-8') as f:
            yamlDefinitionsString = f.read()
            f.close()

        return yaml.safe_load(yamlDefinitionsString)
