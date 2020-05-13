from injecta.service.class_.InspectedArgument import InspectedArgument
from injecta.service.argument.ServiceArgument import ServiceArgument

class ArgumentResolver:

    def resolve(self, inspectedArgument: InspectedArgument, serviceName: str, classes2Services: dict):
        moduleName = inspectedArgument.dtype.moduleName
        className = inspectedArgument.dtype.className

        if className == '_empty':
            raise Exception('Cannot resolve argument {} for service {}'.format(inspectedArgument.name, serviceName))

        if moduleName not in classes2Services:
            moduleNameStripped = moduleName[:moduleName.rfind('.')]

            if moduleNameStripped in classes2Services:
                raise Exception('Consider changing service dtype from {} -> {} (invalid dtype)'.format(moduleNameStripped + '.' + className, moduleName + '.' + className))

            raise Exception('Service not found for {} used in {}'.format(moduleName + '.' + className, serviceName))

        if className not in classes2Services[moduleName]:
            raise Exception('Service not found for {} used in {}'.format(moduleName + '.' + className, serviceName))

        if len(classes2Services[moduleName][className]) > 1:
            serviceNames = ', '.join(classes2Services[moduleName][className])
            raise Exception('Multiple services of dtype {} in dtype {} defined ({}), dtype used in service {}'.format(className, moduleName, serviceNames, serviceName))

        return ServiceArgument(classes2Services[moduleName][className][0], inspectedArgument.name)
