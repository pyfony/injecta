from Injecta.Argument.ServiceArgument import ServiceArgument
from Injecta.Argument.ParameterArgument import ParameterArgument
from Injecta.Argument.ValueArgument import ValueArgument

class ArgumentParser:

    def parse(self, argument):
        if isinstance(argument, str):
            if argument[0:1] == '@':
                return ServiceArgument(argument[1:])
            elif argument[0:1] == '%' and argument[-1:] == '%':
                return ParameterArgument(argument[1:-1])
            else:
                return ValueArgument(argument)
        elif isinstance(argument, list):
            return list(map(lambda argument2: self.parse(argument2), argument))
        elif isinstance(argument, dict):
            output = {}

            for key, value in argument.items():
                output[key] = self.parse(value)

            return output
        else:
            raise Exception('Unexpected argument type')
