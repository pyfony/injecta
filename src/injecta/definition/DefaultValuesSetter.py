from typing import List
from injecta.definition.argument.ArgumentInterface import ArgumentInterface
from injecta.definition.argument.PrimitiveArgument import PrimitiveArgument
from injecta.service.class_.ConstructorArgument import ConstructorArgument

class DefaultValuesSetter:

    def set(self, arguments: List[ArgumentInterface], constructorArguments: List[ConstructorArgument]):
        newArguments = []

        i = 1
        for constructorArgument in constructorArguments:
            if i <= len(arguments):
                newArguments.append(arguments[i - 1])
            elif constructorArgument.defaultValue is not None:
                newArguments.append(PrimitiveArgument(constructorArgument.defaultValue))

            i += 1

        return newArguments
