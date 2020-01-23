from pathlib import Path
import os
from injecta.dtype.classLoader import loadClass
from injecta.container.ContainerInterface import ContainerInterface
from injecta.bundle.appConfigLoader import loadAppConfig

def initAppContainer(appEnv: str) -> ContainerInterface:
    workingDir = Path(os.getcwd())

    appConfig = loadAppConfig(workingDir.joinpath('pyproject.toml'))
    containerInitConfig = appConfig['container-init']

    initContainerFunction = loadClass(containerInitConfig[0], containerInitConfig[1])

    return initContainerFunction(appEnv)
