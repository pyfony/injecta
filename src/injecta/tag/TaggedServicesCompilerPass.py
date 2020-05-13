from injecta.compiler.CompilerPassInterface import CompilerPassInterface
from injecta.container.ContainerBuild import ContainerBuild
from injecta.service.resolved.ResolvedArgument import ResolvedArgument
from injecta.service.resolved.ResolvedService import ResolvedService
from injecta.tag.TaggedArgumentResolver import TaggedArgumentResolver

class TaggedServicesCompilerPass(CompilerPassInterface):

    def __init__(self):
        self.__taggedArgumentResolver = TaggedArgumentResolver()

    def process(self, containerBuild: ContainerBuild):
        for resolvedService in containerBuild.resolvedServices:
            resolvedArguments = self.__resolveArguments(resolvedService, containerBuild)

            resolvedService.replaceResolvedArguments(resolvedArguments)

    def __resolveArguments(self, resolvedService: ResolvedService, containerBuild: ContainerBuild):
        def resolveArgument(resolvedArgument: ResolvedArgument):
            return self.__taggedArgumentResolver.resolve(resolvedArgument, containerBuild)

        return list(map(resolveArgument, resolvedService.resolvedArguments))
