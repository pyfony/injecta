from injecta.service.resolved.ResolvedArgument import ResolvedArgument
from injecta.service.resolved.ResolvedService import ResolvedService


class ObjectGenerator:
    def generate(self, resolved_service: ResolvedService):
        service = resolved_service.service
        argument_lines = list(map(self.__create_argument_line, resolved_service.resolved_arguments))

        if service.uses_factory():
            return (
                "        return "
                + service.factory_service.get_string_value()
                + "."
                + service.factory_method
                + "("
                + ", ".join(argument_lines)
                + ")"
            )

        return (
            "        from " + service.class_.module_name + " import " + service.class_.class_name + "\n"
            "\n"
            "        return " + service.class_.class_name + "(" + ", ".join(argument_lines) + ")"
        )

    def __create_argument_line(self, resolved_argument: ResolvedArgument):
        argument = resolved_argument.argument

        if argument.name is None:
            return argument.get_string_value()

        return argument.name + "=" + argument.get_string_value()
