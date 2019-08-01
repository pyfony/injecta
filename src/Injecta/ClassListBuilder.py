from Injecta.Definition import Definition

class ClassListBuilder:

    def buildClassList(self, definitions: list):
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
