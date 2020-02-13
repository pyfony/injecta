from injecta.compiler.CompilerPassInterface import CompilerPassInterface
from injecta.container.ContainerBuild import ContainerBuild
from injecta.service.Service import Service
from injecta.service.argument.ListArgument import ListArgument
from injecta.service.argument.ServiceArgument import ServiceArgument
from injecta.service.argument.TaggedServicesArgument import TaggedServicesArgument

class TaggedServicesCompilerPass(CompilerPassInterface):

    def process(self, containerBuild: ContainerBuild):
        for service in containerBuild.services:
            newArguments = self.__resolveArguments(service, containerBuild)

            service.setArguments(newArguments)

    def __resolveArguments(self, service: Service, containerBuild: ContainerBuild):
        newArguments = []

        for argument in service.arguments:
            if isinstance(argument, TaggedServicesArgument):
                servicesForTag = containerBuild.getServicesByTag(argument.tagName)
                serviceArguments = list(map(lambda service: ServiceArgument(service.name), servicesForTag))

                newArguments.append(ListArgument(serviceArguments))

            else:
                newArguments.append(argument)

        return newArguments
