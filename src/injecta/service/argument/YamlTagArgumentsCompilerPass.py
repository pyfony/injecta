from injecta.compiler.CompilerPassInterface import CompilerPassInterface
from injecta.container.ContainerBuild import ContainerBuild
from injecta.tag.TaggedAliasedArgumentResolver import TaggedAliasedArgumentResolver
from injecta.service.resolved.ResolvedArgument import ResolvedArgument
from injecta.service.resolved.ResolvedService import ResolvedService
from injecta.tag.TaggedArgumentResolver import TaggedArgumentResolver


class YamlTagArgumentsCompilerPass(CompilerPassInterface):
    def __init__(self):
        self.__tagged_argument_resolver = TaggedArgumentResolver()
        self.__tagged_aliased_argument_resolver = TaggedAliasedArgumentResolver()

    def process(self, container_build: ContainerBuild):
        for resolved_service in container_build.resolved_services:
            resolved_arguments = self.__resolve_arguments(resolved_service, container_build)

            resolved_service.replace_resolved_arguments(resolved_arguments)

    def __resolve_arguments(self, resolved_service: ResolvedService, container_build: ContainerBuild):
        def resolve_argument(resolved_argument: ResolvedArgument):
            resolved_argument = self.__tagged_argument_resolver.resolve(resolved_argument, container_build)
            resolved_argument = self.__tagged_aliased_argument_resolver.resolve(resolved_argument, container_build)
            return resolved_argument

        return list(map(resolve_argument, resolved_service.resolved_arguments))
