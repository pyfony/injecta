from typing import List, Dict, Any
from box import Box
from injecta.definition.Definition import Definition
from injecta.service.Service import Service

class ContainerBuild:

    def __init__(
        self,
        parameters: Dict[Any, Box],
        services: List[Service],
        classes2Services: dict,
        tag2Definitions: Dict[str, List[Definition]],
        appEnv: str
    ):
        self.__parameters = parameters
        self.__services = services
        self.__classes2Services = classes2Services
        self.__tag2Definitions = tag2Definitions
        self.__appEnv = appEnv

    @property
    def services(self) -> List[Service]:
        return self.__services

    @property
    def parameters(self) -> Dict[Any, Box]:
        return self.__parameters

    @property
    def definitions(self) -> List[Definition]:
        return list(map(lambda service: service.definition, self.__services))

    @property
    def classes2Services(self):
        return self.__classes2Services

    @property
    def appEnv(self) -> str:
        return self.__appEnv

    def getServicesByTag(self, tagName) -> List[Definition]:
        if tagName not in self.__tag2Definitions:
            return []

        return self.__tag2Definitions[tagName]
