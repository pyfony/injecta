from injecta.compiler.CompilerPassInterface import CompilerPassInterface
from injecta.container.ContainerBuild import ContainerBuild
from injecta.definition.Definition import Definition
from injecta.definition.argument.ListArgument import ListArgument
from injecta.definition.argument.ServiceArgument import ServiceArgument
from injecta.definition.argument.TaggedServicesArgument import TaggedServicesArgument

class TaggedServicesCompilerPass(CompilerPassInterface):

    def process(self, containerBuild: ContainerBuild):
        for definition in containerBuild.definitions:
            newArguments = self.__resolveArguments(definition, containerBuild)

            definition.setArguments(newArguments)

    def __resolveArguments(self, definition: Definition, containerBuild: ContainerBuild):
        newArguments = []

        for argument in definition.arguments:
            if isinstance(argument, TaggedServicesArgument):
                definitionsForTag = containerBuild.getServicesByTag(argument.tagName)
                serviceArguments = list(map(lambda definition: ServiceArgument(definition.name), definitionsForTag))

                newArguments.append(ListArgument(serviceArguments))

            else:
                newArguments.append(argument)

        return newArguments
