from typing import List
from injecta.service.argument.ArgumentInterface import ArgumentInterface
from injecta.service.argument.PrimitiveArgument import PrimitiveArgument
from injecta.service.class_.InspectedArgument import InspectedArgument

class DefaultValuesSetter:

    def set(self, arguments: List[ArgumentInterface], inspectedArguments: List[InspectedArgument]):
        newArguments = []

        i = 1
        for inspectedArgument in inspectedArguments:
            if i <= len(arguments):
                newArguments.append(arguments[i - 1])
            elif inspectedArgument.defaultValue is not None:
                newArguments.append(PrimitiveArgument(inspectedArgument.defaultValue))

            i += 1

        return newArguments
