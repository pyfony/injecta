from typing import List, Dict, Any
from box import Box
from injecta.service.Service import Service
from injecta.service.resolved.ResolvedService import ResolvedService


class ContainerBuild:
    def __init__(
        self,
        parameters: Dict[Any, Box],
        resolved_services: List[ResolvedService],
        classes2_services: dict,
        aliases2_services: dict,
        tag2_services: Dict[str, List[Service]],
    ):
        self.__parameters = parameters
        self.__resolved_services = resolved_services
        self.__classes2_services = classes2_services
        self.__aliases2_services = aliases2_services
        self.__tag2_services = tag2_services

    @property
    def resolved_services(self) -> List[ResolvedService]:
        return self.__resolved_services

    @property
    def parameters(self) -> Dict[Any, Box]:
        return self.__parameters

    @property
    def services(self) -> List[Service]:
        return list(map(lambda resolved_service: resolved_service.service, self.__resolved_services))

    @property
    def classes2_services(self):
        return self.__classes2_services

    @property
    def aliases2_services(self) -> dict:
        return self.__aliases2_services

    def get_services_by_tag(self, tag_name) -> List[Service]:
        if tag_name not in self.__tag2_services:
            return []

        return self.__tag2_services[tag_name]
