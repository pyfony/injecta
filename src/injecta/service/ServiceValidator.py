from typing import List
from injecta.definition.argument.ArgumentInterface import ArgumentInterface
from injecta.service.ServiceValidatorException import ServiceValidatorException
from injecta.service.class_.ConstructorArgument import ConstructorArgument

class ServiceValidator:

    def validate(
        self,
        serviceName: str,
        definitionArguments: List[ArgumentInterface],
        constructorArguments: List[ConstructorArgument],
        services2Classes: dict
    ):
        for index, argument in enumerate(definitionArguments):
            try:
                constructorArgument = constructorArguments[index]
            except IndexError:
                raise Exception('More arguments defined than given for "{}"'.format(serviceName))

            if constructorArgument.dtype.isDefined():
                try:
                    argument.checkTypeMatchesDefinition(constructorArgument, services2Classes)
                except ServiceValidatorException as e:
                    raise e.createFinalException(serviceName)
