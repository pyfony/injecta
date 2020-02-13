from injecta.schema.ServiceSchemaValidator import ServiceSchemaValidator

class SchemaValidator:

    def __init__(self):
        self.__serviceDefinitionSchemaValidator = ServiceSchemaValidator()

    def validate(self, services: dict):
        for serviceName, rawServiceDefinition in services.items():
            self.__serviceDefinitionSchemaValidator.validate(serviceName, rawServiceDefinition)
