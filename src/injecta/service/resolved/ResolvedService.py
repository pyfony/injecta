from typing import List
from injecta.service.Service import Service
from injecta.service.resolved.ResolvedArgument import ResolvedArgument


class ResolvedService:
    def __init__(
        self,
        service: Service,
        resolved_arguments: List[ResolvedArgument],
    ):
        self.__service = service
        self.__resolved_arguments = resolved_arguments

    @property
    def service(self):
        return self.__service

    @property
    def resolved_arguments(self):
        return self.__resolved_arguments

    def replace_resolved_arguments(self, resolved_arguments: List[ResolvedArgument]):
        self.__resolved_arguments = resolved_arguments

    def __eq__(self, other: "ResolvedService"):
        return self.service == other.service and self.__resolved_arguments == other.resolved_arguments
