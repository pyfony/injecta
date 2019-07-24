class ClassListBuilder:

    def buildClassList(self, definitions: list):
        classes = {}

        for definition in definitions:
            if definition.getClassFqn() not in classes:
                classes[definition.getClassFqn()] = []
            
            classes[definition.getClassFqn()].append(definition.getName())

        return classes
