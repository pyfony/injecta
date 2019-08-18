from Injecta.Argument.ServiceArgument import ServiceArgument

class ArgumentResolver:

    def resolve(self, argumentName: str, moduleName: str, className: str, serviceName: str, classes: dict):
        if className == '_empty':
            raise Exception('Cannot resolve argument {} for service {}'.format(argumentName, serviceName))

        if moduleName not in classes:
            moduleNameStripped = moduleName[:moduleName.rfind('.')]

            if moduleNameStripped in classes:
                raise Exception('Consider changing service class from {} -> {} (invalid module)'.format(moduleNameStripped + '.' + className, moduleName + '.' + className))

            raise Exception('Service not found for {} used in {}'.format(moduleName + '.' + className, serviceName))

        if className not in classes[moduleName]:
            raise Exception('Service not found for {} used in {}'.format(moduleName + '.' + className, serviceName))

        if len(classes[moduleName][className]) > 1:
            serviceNames = ', '.join(classes[moduleName][className])
            raise Exception('Multiple services of class {} in module {} defined ({}), class used in service {}'.format(className, moduleName, serviceNames, serviceName))

        return ServiceArgument(classes[moduleName][className][0])
