class ArgumentsValidatorException(Exception):
    def __init__(self, argument_mame: str, argument_type: str, service_class_type: str):
        self.__argument_mame = argument_mame
        self.__argument_type = argument_type
        self.__service_class_type = service_class_type

        super().__init__()

    def create_final_exception(self, service_name: str):
        argument_type = self.__argument_type.replace("builtins.", "")

        raise Exception(
            'Expected dtype "{}", got "{}" (argument "{}", service "{}")'.format(
                argument_type,
                self.__service_class_type,
                self.__argument_mame,
                service_name,
            )
        )
