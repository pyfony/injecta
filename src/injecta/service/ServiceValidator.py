from typing import List
from injecta.service.argument.ArgumentInterface import ArgumentInterface
from injecta.service.ServiceValidatorException import ServiceValidatorException
from injecta.service.class_.InspectedArgument import InspectedArgument

class ServiceValidator:

    def validate(
        self,
        serviceName: str,
        serviceArguments: List[ArgumentInterface],
        inspectedArguments: List[InspectedArgument],
        services2Classes: dict
    ):
        for index, argument in enumerate(serviceArguments):
            try:
                inspectedArgument = inspectedArguments[index]
            except IndexError:
                raise Exception('More arguments defined than given for "{}"'.format(serviceName))

            if inspectedArgument.dtype.isDefined():
                try:
                    argument.checkTypeMatchesDefinition(inspectedArgument, services2Classes)
                except ServiceValidatorException as e:
                    raise e.createFinalException(serviceName)
