from typing import List
from injecta.service.argument.validator.ArgumentsValidatorException import ArgumentsValidatorException
from injecta.service.resolved.ResolvedArgument import ResolvedArgument

class ArgumentsValidator:

    def validate(
        self,
        serviceName: str,
        resolvedArguments: List[ResolvedArgument],
        services2Classes: dict,
        aliases2Services: dict,
    ):
        for resolvedArgument in resolvedArguments:
            argument = resolvedArgument.argument
            inspectedArgument = resolvedArgument.inspectedArgument

            if argument and inspectedArgument and inspectedArgument.dtype.isDefined():
                try:
                    argument.checkTypeMatchesDefinition(inspectedArgument, services2Classes, aliases2Services)
                except ArgumentsValidatorException as e:
                    raise e.createFinalException(serviceName)
