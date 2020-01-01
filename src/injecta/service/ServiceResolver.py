from injecta.service.Service import Service
from injecta.service.ServiceValidator import ServiceValidator
from injecta.definition.Definition import Definition
from injecta.service.class_.ConstructorArgumentsResolver import ConstructorArgumentsResolver

class ServiceResolver:

    def __init__(self):
        self.__constructorArgumentsResolver = ConstructorArgumentsResolver()
        self.__serviceValidator = ServiceValidator()

    def resolve(self, definition: Definition, services2Classes: dict) -> Service:
        constructorArguments = self.__constructorArgumentsResolver.resolve(definition.class_)

        if definition.usesFactory() is False:
            self.__serviceValidator.validate(
                definition.name,
                definition.arguments,
                constructorArguments,
                services2Classes
            )

        return Service(definition, constructorArguments)
