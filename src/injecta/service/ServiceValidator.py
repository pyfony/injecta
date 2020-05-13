from typing import List
from injecta.service.ServiceValidatorException import ServiceValidatorException
from injecta.service.resolved.ResolvedArgument import ResolvedArgument

class ServiceValidator:

    def validate(
        self,
        serviceName: str,
        resolvedArguments: List[ResolvedArgument],
        services2Classes: dict
    ):
        for resolvedArgument in resolvedArguments:
            argument = resolvedArgument.argument
            inspectedArgument = resolvedArgument.inspectedArgument

            if argument and inspectedArgument and inspectedArgument.dtype.isDefined():
                try:
                    argument.checkTypeMatchesDefinition(inspectedArgument, services2Classes)
                except ServiceValidatorException as e:
                    raise e.createFinalException(serviceName)
