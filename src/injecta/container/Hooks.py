from typing import List, Tuple
from box import Box
from injecta.container.ContainerBuild import ContainerBuild
from injecta.service.Service import Service
from injecta.service.ServiceAlias import ServiceAlias

class Hooks:

    def start(self, rawConfig: dict) -> dict:
        return rawConfig

    def servicesPrepared(self, services: List[Service], aliases: List[ServiceAlias], parameters: Box) -> Tuple[List[Service], List[ServiceAlias]]: # pylint: disable = unused-argument
        return services, aliases

    def getCustomParameters(self) -> dict:
        return {}

    def parametersParsed(self, parameters: Box) -> Box:
        return parameters

    def containerBuildReady(self, containerBuild: ContainerBuild):
        pass
