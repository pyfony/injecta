from typing import List
from injecta.service.Service import Service


class Classes2ServicesBuilder:
    def build(self, services: List[Service]):
        classes = {}

        for service in services:
            module_name = service.class_.module_name
            class_name = service.class_.class_name

            if module_name not in classes:
                classes[module_name] = {}

            if class_name not in classes[module_name]:
                classes[module_name][class_name] = []

            classes[module_name][class_name].append(service.name)

        return classes
