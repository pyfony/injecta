from typing import List
from injecta.service.Service import Definition

class Classes2ServicesBuilder:

    def build(self, definitions: List[Definition]):
        classes = {}

        for definition in definitions:
            moduleName = definition.class_.moduleName
            className = definition.class_.className

            if moduleName not in classes:
                classes[moduleName] = {}

            if className not in classes[moduleName]:
                classes[moduleName][className] = []

            classes[moduleName][className].append(definition.name)

        return classes
