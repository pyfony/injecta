from typing import List, Tuple
from box import Box
from injecta.container.ContainerBuild import ContainerBuild
from injecta.service.Service import Service
from injecta.service.ServiceAlias import ServiceAlias


class Hooks:
    def start(self, raw_config: dict) -> dict:
        return raw_config

    def services_prepared(
        self, services: List[Service], aliases: List[ServiceAlias], parameters: Box
    ) -> Tuple[List[Service], List[ServiceAlias]]:
        return services, aliases

    def get_custom_parameters(self) -> dict:
        return {}

    def parameters_parsed(self, parameters: Box) -> Box:
        return parameters

    def container_build_ready(self, container_build: ContainerBuild):
        pass
