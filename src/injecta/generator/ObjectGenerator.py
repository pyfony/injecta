from injecta.definition.Definition import Definition

class ObjectGenerator:

    def generate(self, definition: Definition):
        argumentLines = list(map(lambda argument: argument.getStringValue(), definition.arguments))

        if definition.factoryService is not None:
            return (
                '        return ' + definition.factoryService.getStringValue() + '.' + definition.factoryMethod + '(' + ', '.join(argumentLines) + ')'
            )

        return (
            '        from ' + definition.class_.moduleName + ' import ' + definition.class_.className + '\n'
            '\n'
            '        return ' + definition.class_.className + '(' + ', '.join(argumentLines) + ')'
        )
