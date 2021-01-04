from typing import List
from box import Box
from injecta.container.ContainerBuild import ContainerBuild
from injecta.service.Service import Service

class Hooks:

    def start(self, rawConfig: dict) -> dict:
        return rawConfig

    def servicesPrepared(self, services: List[Service]) -> List[Service]:
        return services

    def getCustomParameters(self) -> dict:
        return {}

    def parametersParsed(self, parameters: Box) -> Box:
        return parameters

    def containerBuildReady(self, containerBuild: ContainerBuild):
        pass
