from pathlib import Path
import os
from injecta.dtype.classLoader import loadClass
from injecta.container.ContainerInterface import ContainerInterface
from injecta.bundle.appConfigLoader import loadAppConfig

def initAppContainer(appEnv: str) -> ContainerInterface:
    currentDir = os.path.dirname(os.path.abspath(__file__))
    projectRoot = Path(currentDir).parent.parent.parent.parent.parent

    appConfig = loadAppConfig(projectRoot.joinpath('pyproject.toml'))
    containerInitConfig = appConfig['container-init']

    initContainerFunction = loadClass(containerInitConfig[0], containerInitConfig[1])

    return initContainerFunction(appEnv)
