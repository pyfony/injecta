from box import Box
from Injecta.ContainerInterface import ContainerInterface
from Injecta.CodeGenerator.ServiceMethodNameTranslator import ServiceMethodNameTranslator

def DIService(method):
    def wrapper(*args):
        service_name = method.__name__
        container = args[0]

        if not service_name in container.services:
            # print('creating service ' + service_name)
            container.services[service_name] = method(*args)

        return container.services[service_name]

    return wrapper

class Container(ContainerInterface):

    def __init__(self, config: Box):
        self.__config = config
        self.services = {}
        self.__serviceMethodNameTranslator = ServiceMethodNameTranslator()

    def getConfig(self) -> Box:
        return self.__config

    def get(self, name):
        if hasattr(name, '__module__'):
            name = name.__module__

        methodName = self.__serviceMethodNameTranslator.translate(name)
        method = getattr(self, '_Container{}'.format(methodName))

        return method()
