from Injecta.Service.Definition import Definition

class ObjectGenerator:

    def generate(self, definition: Definition):
        argumentLines = list(map(self.__stringifyArgument, definition.getArguments()))

        if definition.getFactoryService() is not None:
            return (
                '        return ' + definition.getFactoryService().getValue() + '.' + definition.getFactoryMethod() + '(' + ', '.join(argumentLines) + ')'
            )

        return (
            '        from ' + definition.getModuleClass().getModuleName() + ' import ' + definition.getModuleClass().getClassName() + '\n'
            '\n'
            '        return ' + definition.getModuleClass().getClassName() + '(' + ', '.join(argumentLines) + ')'
        )

    def __stringifyArgument(self, argument):
        if isinstance(argument, list):
            argumentList = list(map(self.__stringifyArgument, argument))
            return '[' + ', '.join(argumentList) + ']'

        if isinstance(argument, dict):
            output = []

            for key, subArgument in argument.items():
                output.append('{} = {}'.format(key, subArgument.getValue()))

            return ', '.join(output)

        return argument.getValue()
