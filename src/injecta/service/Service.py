from typing import List
from injecta.definition.Definition import Definition
from injecta.service.class_.ConstructorArgument import ConstructorArgument

class Service:

    def __init__(
        self,
        definition: Definition,
        constructorArguments: List[ConstructorArgument],
    ):
        self.__definition = definition
        self.__constructorArguments = constructorArguments

    @property
    def definition(self):
        return self.__definition

    @property
    def constructorArguments(self):
        return self.__constructorArguments

    def __eq__(self, other: 'Service'):
        return (
            self.definition == other.definition
            and self.constructorArguments == other.constructorArguments
        )
