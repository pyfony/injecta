from typing import List
from injecta.service.argument.validator.ArgumentsValidatorException import ArgumentsValidatorException
from injecta.service.resolved.ResolvedArgument import ResolvedArgument


class ArgumentsValidator:
    def validate(
        self,
        service_name: str,
        resolved_arguments: List[ResolvedArgument],
        services2_classes: dict,
        aliases2_services: dict,
    ):
        for resolved_argument in resolved_arguments:
            argument = resolved_argument.argument
            inspected_argument = resolved_argument.inspected_argument

            if argument and inspected_argument and inspected_argument.dtype.is_defined():
                try:
                    argument.check_type_matches_definition(inspected_argument, services2_classes, aliases2_services)
                except ArgumentsValidatorException as e:
                    raise e.create_final_exception(service_name)
