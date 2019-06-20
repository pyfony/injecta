from Injecta.Definition import Definition

class ObjectGenerator:
   
    def generate(self, definition: Definition):
        argumentLines = list(map(lambda argument: self.__stringifyArgument(argument), definition.getArguments()))

        return (
            'return ' + definition.getClassName() + '(' + ', '.join(argumentLines) + ')'
        )

    def __stringifyArgument(self, argument):
        if isinstance(argument, list):
            argumentList = list(map(lambda subArgument: self.__stringifyArgument(subArgument), argument))
            return '[' + ', '.join(argumentList) + ']'
        elif isinstance(argument, dict):
            output = []

            for key, subArgument in argument.items():
                output.append('{} = {}'.format(key, subArgument.getValue()))

            return ', '.join(output)
        else:
            return argument.getValue()
