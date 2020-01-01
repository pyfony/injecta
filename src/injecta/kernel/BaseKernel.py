from typing import List
from injecta.bundle.Bundle import Bundle
from injecta.config.ConfigReaderInterface import ConfigReaderInterface
from injecta.container.ContainerInitializer import ContainerInitializer
from injecta.container.ContainerInterface import ContainerInterface
from injecta.container.ContainerBuilder import ContainerBuilder

class BaseKernel:

    _allowedEnvironments = ['dev', 'test', 'prod']

    def __init__(
        self,
        appEnv: str,
        configDir: str,
        configReader: ConfigReaderInterface
    ):
        if appEnv not in self._allowedEnvironments:
            raise Exception('Unexpected environment: {}'.format(appEnv))

        self._appEnv = appEnv
        self._configDir = configDir
        self.__configReader = configReader
        self._containerBuilder = ContainerBuilder()

    def initContainer(self) -> ContainerInterface:
        configPath = self._getConfigPath()

        containerBuild = self._containerBuilder.build(
            self.__configReader.read(configPath),
            self._registerBundles(),
            self._appEnv,
            configPath,
        )

        container = ContainerInitializer().init(containerBuild)

        self._boot(container)

        return container

    def _getConfigPath(self):
        return self._configDir + '/config_{}.yaml'.format(self._appEnv)

    def _registerBundles(self) -> List[Bundle]:
        return []

    def _boot(self, container: ContainerInterface):
        for bundle in self._registerBundles():
            bundle.boot(container)
