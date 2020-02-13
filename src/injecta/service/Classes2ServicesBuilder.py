from typing import List
from injecta.service.Service import Service

class Classes2ServicesBuilder:

    def build(self, services: List[Service]):
        classes = {}

        for service in services:
            moduleName = service.class_.moduleName
            className = service.class_.className

            if moduleName not in classes:
                classes[moduleName] = {}

            if className not in classes[moduleName]:
                classes[moduleName][className] = []

            classes[moduleName][className].append(service.name)

        return classes
