from injecta.container.ContainerBuild import ContainerBuild
from injecta.service.argument.ListArgument import ListArgument
from injecta.service.argument.ServiceArgument import ServiceArgument
from injecta.service.argument.TaggedServicesArgument import TaggedServicesArgument
from injecta.service.resolved.ResolvedArgument import ResolvedArgument


class TaggedArgumentResolver:
    def resolve(self, resolved_argument: ResolvedArgument, container_build: ContainerBuild):
        argument = resolved_argument.argument

        if not isinstance(argument, TaggedServicesArgument):
            return resolved_argument

        services_for_tag = container_build.get_services_by_tag(argument.tag_name)
        service_arguments = list(map(lambda service: ServiceArgument(service.name), services_for_tag))

        resolved_argument.modify_argument(ListArgument(service_arguments, argument.name), "tags")
        return resolved_argument
