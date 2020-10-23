from injecta.compiler.CompilerPassInterface import CompilerPassInterface
from injecta.container.ContainerBuild import ContainerBuild
from injecta.tag.TaggedAliasedArgumentResolver import TaggedAliasedArgumentResolver
from injecta.service.resolved.ResolvedArgument import ResolvedArgument
from injecta.service.resolved.ResolvedService import ResolvedService
from injecta.tag.TaggedArgumentResolver import TaggedArgumentResolver

class YamlTagArgumentsCompilerPass(CompilerPassInterface):

    def __init__(self):
        self.__taggedArgumentResolver = TaggedArgumentResolver()
        self.__taggedAliasedArgumentResolver = TaggedAliasedArgumentResolver()

    def process(self, containerBuild: ContainerBuild):
        for resolvedService in containerBuild.resolvedServices:
            resolvedArguments = self.__resolveArguments(resolvedService, containerBuild)

            resolvedService.replaceResolvedArguments(resolvedArguments)

    def __resolveArguments(self, resolvedService: ResolvedService, containerBuild: ContainerBuild):
        def resolveArgument(resolvedArgument: ResolvedArgument):
            resolvedArgument = self.__taggedArgumentResolver.resolve(resolvedArgument, containerBuild)
            resolvedArgument = self.__taggedAliasedArgumentResolver.resolve(resolvedArgument, containerBuild)
            return resolvedArgument

        return list(map(resolveArgument, resolvedService.resolvedArguments))
