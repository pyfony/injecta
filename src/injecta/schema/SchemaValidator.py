from injecta.schema.ServiceDefinitionSchemaValidator import ServiceDefinitionSchemaValidator

class SchemaValidator:

    def __init__(self):
        self.__serviceDefinitionSchemaValidator = ServiceDefinitionSchemaValidator()

    def validate(self, services: dict):
        for serviceName, rawServiceDefinition in services.items():
            self.__serviceDefinitionSchemaValidator.validate(serviceName, rawServiceDefinition)
