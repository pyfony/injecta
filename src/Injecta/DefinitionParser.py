from Injecta.Definition import Definition
from Injecta.Argument.ServiceArgument import ServiceArgument
from Injecta.Argument.ParameterArgument import ParameterArgument
from Injecta.Argument.ValueArgument import ValueArgument

class DefinitionParser:
    
    def parse(self, serviceName: str, serviceDefinition):
        if serviceDefinition is None:
            return Definition(serviceName, serviceName)

        arguments = self.__parseArguments(serviceDefinition)
        tags = serviceDefinition['tags'] if 'tags' in serviceDefinition else []
        classFqn = serviceDefinition['class'] if 'class' in serviceDefinition else serviceName

        definition = Definition(serviceName, classFqn, arguments, tags)

        if 'import' in serviceDefinition:
            definition.setImport(serviceDefinition['import'])

        if 'autowire' in serviceDefinition:
            definition.setAutowire(serviceDefinition['autowire'] == 'True')

        return definition

    def __parseArguments(self, serviceDefinition):
        arguments = []

        if 'arguments' in serviceDefinition:
            arguments = list(map(lambda argument: self.__parseArgument(argument), serviceDefinition['arguments']))

        return arguments

    def __parseArgument(self, argument):
        if isinstance(argument, str):
            if argument[0:1] == '@':
                return ServiceArgument(argument[1:])
            elif argument[0:1] == '%' and argument[-1:] == '%':
                return ParameterArgument(argument[1:-1])
            else:
                return ValueArgument(argument)
        elif isinstance(argument, list):
            return list(map(lambda argument2: self.__parseArgument(argument2), argument))
        elif isinstance(argument, dict):
            output = {}

            for key, value in argument.items():
                output[key] = self.__parseArgument(value)

            return output
        else:
            raise Exception('Unexpected argument type')
