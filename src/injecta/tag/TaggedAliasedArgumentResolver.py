from injecta.container.ContainerBuild import ContainerBuild
from injecta.parameter.all_placeholders_replacer import find_all_placeholders, replace_all_placeholders
from injecta.service.argument.TaggedAliasedServiceArgument import TaggedAliasedServiceArgument
from injecta.service.argument.ServiceArgument import ServiceArgument
from injecta.service.resolved.ResolvedArgument import ResolvedArgument


class TaggedAliasedArgumentResolver:
    def resolve(self, resolved_argument: ResolvedArgument, container_build: ContainerBuild):
        argument = resolved_argument.argument

        if not isinstance(argument, TaggedAliasedServiceArgument):
            return resolved_argument

        services_for_tag = container_build.get_services_by_tag(argument.tag_name)

        if isinstance(argument.tag_alias, str):
            tag_alias = self.__resolve_parameter_value(argument.tag_alias, container_build.parameters)
        else:
            tag_alias = argument.tag_alias

        for service in services_for_tag:
            tag_attributes = service.get_tag_attributes(argument.tag_name)

            if "alias" not in tag_attributes:
                raise Exception(f'"alias" attribute is missing for tag {argument.tag_name}')

            if tag_attributes["alias"] == tag_alias:
                resolved_argument.modify_argument(ServiceArgument(service.name, argument.name), "tagged_aliased")
                return resolved_argument

        raise Exception(f"No service tagged with {argument.tag_name} found for alias: {tag_alias}")

    def __resolve_parameter_value(self, argument, parameters):
        matches = find_all_placeholders(argument)

        if not matches:
            return argument

        return replace_all_placeholders(argument, matches, parameters, argument)
