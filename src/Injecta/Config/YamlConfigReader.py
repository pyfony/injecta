from pathlib import Path
import yaml
from box import Box

class YamlConfigReader:

    def read(self, parametersPath: str):
        if not Path(parametersPath).is_file():
            raise Exception('{} does not exist'.format(parametersPath))

        with open(parametersPath, 'r', encoding='utf-8') as f:
            yamlDefinitionsString = f.read()
            f.close()

        config = yaml.safe_load(yamlDefinitionsString)

        return Box(config)
