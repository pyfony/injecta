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

    def parametersParsed(self, services: Box) -> Box:
        return services

    def containerBuildReady(self, containerBuild: ContainerBuild):
        return containerBuild
