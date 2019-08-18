import inspect
from Injecta.Service.Definition import Definition
from Injecta.Autowiring.ArgumentResolver import ArgumentResolver

class Autowirer:

    def __init__(self, argumentResolver: ArgumentResolver):
        self.__argumentResolver = argumentResolver

    def autowire(self, definition: Definition, classes: dict):
        if definition.getAutowire() is False:
            return definition

        classDefinition = getattr(definition.getModuleClass().getModule(), definition.getModuleClass().getClassName())

        # constructor is missing
        if '__init__' not in classDefinition.__dict__:
            return definition

        signature = inspect.signature(classDefinition.__init__)

        arguments = definition.getArguments()
        newArguments = []

        i = 1
        for argumentName, argumentValue in signature.parameters.items():
            if argumentName == 'self':
                continue

            if i <= len(arguments):
                newArgument = arguments[i - 1]
            else:
                newArgument = self.__argumentResolver.resolve(
                    argumentName,
                    argumentValue.annotation.__module__,
                    argumentValue.annotation.__name__,
                    definition.getName(),
                    classes
                )

            newArguments.append(newArgument)

            i += 1

        return Definition(
            definition.getName(),
            definition.getModuleClass(),
            newArguments,
            definition.getTags()
        )
