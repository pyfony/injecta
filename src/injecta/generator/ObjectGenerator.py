from injecta.service.resolved.ResolvedArgument import ResolvedArgument
from injecta.service.resolved.ResolvedService import ResolvedService

class ObjectGenerator:

    def generate(self, resolvedService: ResolvedService):
        service = resolvedService.service
        argumentLines = list(map(self.__createArgumentLine, resolvedService.resolvedArguments))

        if service.usesFactory():
            return (
                '        return ' + service.factoryService.getStringValue() + '.' + service.factoryMethod + '(' + ', '.join(argumentLines) + ')'
            )

        return (
            '        from ' + service.class_.moduleName + ' import ' + service.class_.className + '\n'
            '\n'
            '        return ' + service.class_.className + '(' + ', '.join(argumentLines) + ')'
        )

    def __createArgumentLine(self, resolvedArgument: ResolvedArgument):
        argument = resolvedArgument.argument

        if argument.name is None:
            return argument.getStringValue()

        return argument.name + '=' + argument.getStringValue()
