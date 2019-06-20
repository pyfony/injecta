import inspect
from Injecta.Definition import Definition
from Injecta.CodeGenerator.ServiceGenerator import ServiceGenerator
from Injecta.Argument.ServiceArgument import ServiceArgument

class ArgumentResolver:

    def resolve(self, argumentName: str, argumentValue, definition: Definition, classes: dict):
        annotation = argumentValue.annotation

        classNameFromModule = annotation.__module__[annotation.__module__.rfind('.') + 1:]

        if classNameFromModule == annotation.__name__:
            classFqn = annotation.__module__
        else:
            moduleStripped = annotation.__module__[:annotation.__module__.rfind('.')]

            classFqn = moduleStripped + '.' + annotation.__name__

        if annotation.__name__ == '_empty':
            raise Exception('Cannot resolve argument {} for service {}'.format(argumentName, definition.getName()))

        if classFqn not in classes:
            raise Exception('Service not found for {} used in {}'.format(classFqn, definition.getClassFqn()))
            
        if len(classes[classFqn]) > 1:
            serviceNames = ', '.join(classes[classFqn])
            raise Exception('Multiple services of {} defined ({}), class used in {}'.format(classFqn, serviceNames, definition.getClassFqn()))

        return ServiceArgument(classes[classFqn][0])
