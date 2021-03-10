from injecta.schema.ServiceSchemaValidator import ServiceSchemaValidator


class SchemaValidator:
    def __init__(self):
        self.__service_definition_schema_validator = ServiceSchemaValidator()

    def validate(self, services: dict):
        for service_name, raw_service_definition in services.items():
            self.__service_definition_schema_validator.validate(service_name, raw_service_definition)
