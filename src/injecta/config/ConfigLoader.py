import yaml
from pathlib import Path

class TaggedServices(yaml.YAMLObject):
    yaml_loader = yaml.SafeLoader
    yaml_tag = '!tagged'
    def __init__(self, val):
        self.val = val

    @classmethod
    def from_yaml(cls, loader, node):
        return cls(node.value)

class TaggedAliasedService(yaml.YAMLObject):
    yaml_loader = yaml.SafeLoader
    yaml_tag = '!tagged_aliased'
    def __init__(self, tagName, tagAlias):
        self.tagName = tagName
        self.tagAlias = tagAlias

    @classmethod
    def from_yaml(cls, loader, node):
        return cls(node.value[0].value, node.value[1].value)

class ConfigLoader:

    def load(self, configPath: Path):
        if not Path(configPath).is_file():
            raise Exception('{} does not exist'.format(configPath))

        with configPath.open('r', encoding='utf-8') as f:
            yamlConfigString = f.read()
            f.close()

        return yaml.safe_load(yamlConfigString)
