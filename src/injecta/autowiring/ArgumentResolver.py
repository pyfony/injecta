from injecta.service.class_.InspectedArgument import InspectedArgument
from injecta.service.argument.ServiceArgument import ServiceArgument


class ArgumentResolver:
    def resolve(self, inspected_argument: InspectedArgument, service_name: str, classes2_services: dict):
        module_name = inspected_argument.dtype.module_name
        class_name = inspected_argument.dtype.class_name

        if class_name == "_empty":
            raise Exception("Cannot resolve argument {} for service {}".format(inspected_argument.name, service_name))

        if module_name not in classes2_services:
            module_name_stripped = module_name[: module_name.rfind(".")]

            if module_name_stripped in classes2_services:
                raise Exception(
                    "Consider changing service dtype from {} -> {} (invalid dtype)".format(
                        module_name_stripped + "." + class_name, module_name + "." + class_name
                    )
                )

            raise Exception("Service not found for {} used in {}".format(module_name + "." + class_name, service_name))

        if class_name not in classes2_services[module_name]:
            raise Exception("Service not found for {} used in {}".format(module_name + "." + class_name, service_name))

        if len(classes2_services[module_name][class_name]) > 1:
            service_names = ", ".join(classes2_services[module_name][class_name])
            raise Exception(
                "Multiple services of dtype {} in dtype {} defined ({}), dtype used in service {}".format(
                    class_name, module_name, service_names, service_name
                )
            )

        return ServiceArgument(classes2_services[module_name][class_name][0], inspected_argument.name)
