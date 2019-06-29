import inspect
from Injecta.Definition import Definition
from Injecta.CodeGenerator.ServiceGenerator import ServiceGenerator
from Injecta.Argument.ServiceArgument import ServiceArgument
from Injecta.Autowiring.ArgumentResolver import ArgumentResolver

class Autowirer:

    def __init__(self, argumentResolver: ArgumentResolver):
        self.__argumentResolver = argumentResolver

    def autowire(self, definition: Definition, classes: dict):
        if definition.getAutowire() == False:
            return definition

        module = __import__(definition.getClassFqn(), fromlist=[definition.getClassName()])
        classDefinition = getattr(module, definition.getClassName())

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
                    argumentValue,
                    definition,
                    classes
                )
                
            newArguments.append(newArgument)

            i += 1
            
        return Definition(
            definition.getName(),
            definition.getClassFqn(),
            newArguments,
            definition.getTags()
        )
