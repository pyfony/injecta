from pathlib import Path
import tomlkit

def loadAppConfig(pyprojectPath: Path) -> list:
    with pyprojectPath.open('r') as t:
        config = tomlkit.parse(t.read())

        if 'app' not in config:
            raise Exception('[app] section is missing in pyproject.toml')

        return config['app']
