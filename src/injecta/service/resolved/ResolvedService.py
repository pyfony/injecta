from typing import List
from injecta.service.Service import Service
from injecta.service.class_.ConstructorArgument import ConstructorArgument

class ResolvedService:

    def __init__(
        self,
        service: Service,
        constructorArguments: List[ConstructorArgument],
    ):
        self.__service = service
        self.__constructorArguments = constructorArguments

    @property
    def service(self):
        return self.__service

    @property
    def constructorArguments(self):
        return self.__constructorArguments

    def __eq__(self, other: 'ResolvedService'):
        return (
            self.service == other.service
            and self.constructorArguments == other.constructorArguments
        )
