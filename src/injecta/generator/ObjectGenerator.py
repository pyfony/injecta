from injecta.service.Service import Service

class ObjectGenerator:

    def generate(self, service: Service):
        argumentLines = list(map(lambda argument: argument.getStringValue(), service.arguments))

        if service.factoryService is not None:
            return (
                '        return ' + service.factoryService.getStringValue() + '.' + service.factoryMethod + '(' + ', '.join(argumentLines) + ')'
            )

        return (
            '        from ' + service.class_.moduleName + ' import ' + service.class_.className + '\n'
            '\n'
            '        return ' + service.class_.className + '(' + ', '.join(argumentLines) + ')'
        )
