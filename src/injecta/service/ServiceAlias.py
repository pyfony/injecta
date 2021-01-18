class ServiceAlias:

    def __init__(self, name: str, aliasedService: str):
        self.__name = name
        self.__aliasedService = aliasedService

    @property
    def name(self) -> str:
        return self.__name

    @property
    def aliasedService(self) -> str:
        return self.__aliasedService

    def __eq__(self, other: 'ServiceAlias'):
        return (
            self.name == other.name
            and self.aliasedService == other.aliasedService
        )
