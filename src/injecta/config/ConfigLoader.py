import yaml
from pathlib import Path


class TaggedServices(yaml.YAMLObject):
    yaml_loader = yaml.SafeLoader
    yaml_tag = "!tagged"

    def __init__(self, val):
        self.val = val

    @classmethod
    def from_yaml(cls, loader, node):
        return cls(node.value)


class TaggedAliasedService(yaml.YAMLObject):
    yaml_loader = yaml.SafeLoader
    yaml_tag = "!tagged_aliased"

    def __init__(self, tag_name, tag_alias):
        self.tag_name = tag_name
        self.tag_alias = tag_alias

    @classmethod
    def from_yaml(cls, loader, node):
        return cls(node.value[0].value, node.value[1].value)


class ConfigLoader:
    def load(self, config_path: Path):
        if not Path(config_path).is_file():
            raise Exception("{} does not exist".format(config_path))

        with config_path.open("r", encoding="utf-8") as f:
            yaml_config_string = f.read()
            f.close()

        return yaml.safe_load(yaml_config_string)
