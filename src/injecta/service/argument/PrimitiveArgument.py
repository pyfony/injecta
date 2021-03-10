import re
from injecta.service.argument.ArgumentInterface import ArgumentInterface
from injecta.service.argument.validator.ArgumentsValidatorException import ArgumentsValidatorException
from injecta.service.class_.InspectedArgument import InspectedArgument


class PrimitiveArgument(ArgumentInterface):
    def __init__(self, value, name: str = None):
        self.__value = value
        self.__name = name

    @property
    def name(self):
        return self.__name

    def get_string_value(self):
        if isinstance(self.__value, str):
            return self.__get_string_value()

        if isinstance(self.__value, bool):
            return "True" if self.__value is True else "False"

        return str(self.__value)

    def check_type_matches_definition(self, inspected_argument: InspectedArgument, services2_classes: dict, aliases2_services: dict):
        dtype = inspected_argument.dtype

        if dtype.module_name == "box":
            return

        if dtype.is_primitive_type() is False:
            raise ArgumentsValidatorException(inspected_argument.name, str(inspected_argument.dtype), self.__value.__class__.__name__)

    def __get_string_value(self):
        output = self.__value

        if re.match(r"^%env\(([^)]+)\)%$", output):
            return re.sub(r"^%env\(([^)]+)\)%$", "os.environ['\\g<1>']", output)

        if re.match(r"^%([^%]+)%$", output):
            return re.sub(r"^%([^%]+)%$", "self.__parameters.\\g<1>", output)

        output = re.sub(r"%env\(([^)]+)\)%", "' + os.environ['\\g<1>'] + '", output)
        output = re.sub(r"%([^%]+)%", "' + self.__parameters.\\g<1> + '", output)

        output = "'" + output + "'"

        output = re.sub(r" \+ \'\'$", "", output)
        output = re.sub(r"^\'\' \+ ", "", output)

        return output

    def __eq__(self, other: "PrimitiveArgument"):
        return self.name == other.name and self.get_string_value() == other.get_string_value()
