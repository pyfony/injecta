import yaml
from pathlib import Path

class ConfigLoader:

    def load(self, configPath: Path):
        if not Path(configPath).is_file():
            raise Exception('{} does not exist'.format(configPath))

        with configPath.open('r', encoding='utf-8') as f:
            yamlDefinitionsString = f.read()
            f.close()

        return yaml.safe_load(yamlDefinitionsString)
