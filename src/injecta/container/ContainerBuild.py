from typing import List, Dict, Any
from box import Box
from injecta.service.Service import Service
from injecta.service.resolved.ResolvedService import ResolvedService

class ContainerBuild:

    def __init__(
        self,
        parameters: Dict[Any, Box],
        resolvedServices: List[ResolvedService],
        classes2Services: dict,
        aliases2Services: dict,
        tag2Services: Dict[str, List[Service]],
    ):
        self.__parameters = parameters
        self.__resolvedServices = resolvedServices
        self.__classes2Services = classes2Services
        self.__aliases2Services = aliases2Services
        self.__tag2Services = tag2Services

    @property
    def resolvedServices(self) -> List[ResolvedService]:
        return self.__resolvedServices

    @property
    def parameters(self) -> Dict[Any, Box]:
        return self.__parameters

    @property
    def services(self) -> List[Service]:
        return list(map(lambda resolvedService: resolvedService.service, self.__resolvedServices))

    @property
    def classes2Services(self):
        return self.__classes2Services

    @property
    def aliases2Services(self) -> dict:
        return self.__aliases2Services

    def getServicesByTag(self, tagName) -> List[Service]:
        if tagName not in self.__tag2Services:
            return []

        return self.__tag2Services[tagName]
