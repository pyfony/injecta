class ServiceValidatorException(Exception):

    def __init__(self, argumentMame: str, argumentType: str, serviceClassType: str):
        self.__argumentMame = argumentMame
        self.__argumentType = argumentType
        self.__serviceClassType = serviceClassType

        super().__init__()

    def createFinalException(self, serviceName: str):
        argumentType = self.__argumentType.replace('builtins.', '')

        raise Exception('Expected dtype "{}", got "{}" (argument "{}", service "{}")'.format(
            argumentType,
            self.__serviceClassType,
            self.__argumentMame,
            serviceName,
        ))
