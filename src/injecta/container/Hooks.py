from typing import List
from box import Box
from injecta.container.ContainerBuild import ContainerBuild
from injecta.service.Service import Service

class Hooks:

    _servicesTestingModeEnabled = False

    def enableServicesTestingMode(self):
        self._servicesTestingModeEnabled = True

    def start(self, rawConfig: dict) -> dict:
        return rawConfig

    def servicesPrepared(self, services: List[Service]) -> List[Service]:
        return services

    def getCustomParameters(self) -> dict:
        return {
            'container': {
                'servicesTestingModeEnabled': self._servicesTestingModeEnabled
            }
        }

    def parametersParsed(self, parameters: Box) -> Box:
        return parameters

    def containerBuildReady(self, containerBuild: ContainerBuild):
        pass
