class ServiceAlias:
    def __init__(self, name: str, aliased_service: str):
        self.__name = name
        self.__aliased_service = aliased_service

    @property
    def name(self) -> str:
        return self.__name

    @property
    def aliased_service(self) -> str:
        return self.__aliased_service

    def __eq__(self, other: "ServiceAlias"):
        return self.name == other.name and self.aliased_service == other.aliased_service
