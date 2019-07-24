from Injecta.Definition import Definition
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
            className = classFqn[classFqn.rfind('.') + 1:]

            if className in classes:
                affectedServiceName = classes[className][0]
                raise Exception('Setting "class: {}" for service "{}" is likely missing'.format(classFqn, affectedServiceName))
            else:
                raise Exception('Service not found for {} used in {}'.format(classFqn, definition.getName()))

        if len(classes[classFqn]) > 1:
            serviceNames = ', '.join(classes[classFqn])
            raise Exception('Multiple services of {} defined ({}), class used in {}'.format(classFqn, serviceNames, definition.getName()))

        return ServiceArgument(classes[classFqn][0])
