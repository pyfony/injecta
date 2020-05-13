from typing import List
from injecta.service.Service import Service
from injecta.service.class_.InspectedArgument import InspectedArgument

class ResolvedService:

    def __init__(
        self,
        service: Service,
        inspectedArguments: List[InspectedArgument],
    ):
        self.__service = service
        self.__inspectedArguments = inspectedArguments

    @property
    def service(self):
        return self.__service

    @property
    def inspectedArguments(self):
        return self.__inspectedArguments

    def __eq__(self, other: 'ResolvedService'):
        return (
            self.service == other.service
            and self.inspectedArguments == other.inspectedArguments
        )
