from Injecta.Argument.ServiceArgument import ServiceArgument
from Injecta.Argument.ValueArgument import ValueArgument

class ArgumentParser:

    def parse(self, argument):
        if isinstance(argument, str):
            if argument[0:1] == '@':
                return ServiceArgument(argument[1:])

            return ValueArgument(argument)

        if isinstance(argument, list):
            return list(map(self.parse, argument))

        if isinstance(argument, dict):
            output = {}

            for key, value in argument.items():
                output[key] = self.parse(value)

            return output

        raise Exception('Unexpected argument type')
