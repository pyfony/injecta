from typing import List
from injecta.service.Service import Service
from injecta.service.resolved.ResolvedArgument import ResolvedArgument

class ResolvedService:

    def __init__(
        self,
        service: Service,
        resolvedArguments: List[ResolvedArgument],
    ):
        self.__service = service
        self.__resolvedArguments = resolvedArguments

    @property
    def service(self):
        return self.__service

    @property
    def resolvedArguments(self):
        return self.__resolvedArguments

    def replaceResolvedArguments(self, resolvedArguments: List[ResolvedArgument]):
        self.__resolvedArguments = resolvedArguments

    def __eq__(self, other: 'ResolvedService'):
        return (
            self.service == other.service
            and self.__resolvedArguments == other.resolvedArguments
        )
