from typing import List
from Injecta.Service.Definition import Definition

class ClassListBuilder:

    def buildClassList(self, definitions: List[Definition]):
        classes = {}

        for definition in definitions: # type: Definition
            moduleName = definition.getModuleClass().getModuleName()
            className = definition.getModuleClass().getClassName()

            if moduleName not in classes:
                classes[moduleName] = {}

            if className not in classes[moduleName]:
                classes[moduleName][className] = []

            classes[moduleName][className].append(definition.getName())

        return classes
