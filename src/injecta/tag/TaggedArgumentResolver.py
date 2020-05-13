from injecta.container.ContainerBuild import ContainerBuild
from injecta.service.argument.ListArgument import ListArgument
from injecta.service.argument.ServiceArgument import ServiceArgument
from injecta.service.argument.TaggedServicesArgument import TaggedServicesArgument
from injecta.service.resolved.ResolvedArgument import ResolvedArgument

class TaggedArgumentResolver:

    def resolve(self, resolvedArgument: ResolvedArgument, containerBuild: ContainerBuild):
        argument = resolvedArgument.argument

        if not isinstance(argument, TaggedServicesArgument):
            return resolvedArgument

        servicesForTag = containerBuild.getServicesByTag(argument.tagName)
        serviceArguments = list(map(lambda service: ServiceArgument(service.name), servicesForTag))

        resolvedArgument.modifyArgument(ListArgument(serviceArguments, argument.name), 'tags')
        return resolvedArgument
