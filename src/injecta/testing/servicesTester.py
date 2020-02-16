import inspect
from injecta.container.ContainerInterface import ContainerInterface

def testServices(container: ContainerInterface):
    serviceNames = getServiceNames(container)

    for serviceName in serviceNames:
        container.get(serviceName)

def getServiceNames(container: ContainerInterface):
    def servicesOnly(methodName: str, container: ContainerInterface):
        return methodName[0:12] == '_Container__' and inspect.ismethod(getattr(container, methodName))

    containerMethods = list(filter(lambda methodName: servicesOnly(methodName, container), dir(container)))

    def methodName2ServiceName(methodName: str):
        return methodName[12:].replace('_', '.')

    return list(map(methodName2ServiceName, containerMethods))
