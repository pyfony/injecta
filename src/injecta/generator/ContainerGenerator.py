from typing import List
from injecta.generator.ServiceGenerator import ServiceGenerator
from injecta.lib_root import get_lib_root
from injecta.service.resolved.ResolvedService import ResolvedService


class ContainerGenerator:
    def __init__(
        self,
        service_generator: ServiceGenerator,
    ):
        self.__service_generator = service_generator

    def generate(self, resolved_services: List[ResolvedService], aliases2_services: dict):
        path = get_lib_root() + "/generator/container_template.py"

        with open(path, "r", encoding="utf-8") as f:
            output = f.read() + "\n"
            f.close()

        code_of_service_methods = list(map(self.__service_generator.generate, resolved_services))
        code_of_service_alias_methods = [
            self.__service_generator.generate_aliases(alias, service_name) for alias, service_name in aliases2_services.items()
        ]

        output += "\n".join(code_of_service_methods + code_of_service_alias_methods)

        return output
