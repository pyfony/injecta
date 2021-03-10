from injecta.schema.SchemaValidationException import SchemaValidationException


class ServiceSchemaValidator:

    allowed_attributes = ["class", "arguments", "tags", "autowire", "factory"]

    def validate(self, service_name, raw_service_definition):
        if self.__is_basic_definition(raw_service_definition):
            return

        if isinstance(raw_service_definition, str):
            if self.__is_alias(raw_service_definition):
                return

            raise SchemaValidationException(f"Service aliased with {service_name} must be prefixed with @")

        if isinstance(raw_service_definition, list):
            raise SchemaValidationException('Arguments of service "{}" must be defined in the "arguments" key'.format(service_name))

        if isinstance(raw_service_definition, dict) is False:
            raise SchemaValidationException('service "{}" not properly defined'.format(service_name))

        unexpected_attributes = set(raw_service_definition.keys()) - set(ServiceSchemaValidator.allowed_attributes)

        if unexpected_attributes:
            raise SchemaValidationException(
                'Unexpected attributes ({}) for service "{}"'.format(", ".join(unexpected_attributes), service_name)
            )

        # if 'arguments' in raw_service_definition:
        # if isinstance(raw_service_definition['arguments'], list) is False:
        # raise SchemaValidationException('Arguments of service "{}" must be defined as list'.format(service_name))

        if "tags" in raw_service_definition:
            if isinstance(raw_service_definition["tags"], list) is False:
                raise SchemaValidationException('Tags of service "{}" must be defined as list'.format(service_name))

        if "autowire" in raw_service_definition:
            if isinstance(raw_service_definition["autowire"], bool) is False:
                raise SchemaValidationException('Attribute "autowire" of service "{}" must be True or False'.format(service_name))

        if "factory" in raw_service_definition:
            if isinstance(raw_service_definition["factory"], list) is False or (
                isinstance(raw_service_definition["factory"], list) is True and len(raw_service_definition["factory"]) != 2
            ):
                raise SchemaValidationException(
                    'Attribute "factory" of service "{}" must be list [factory_class, factory_method]'.format(service_name)
                )

    def __is_basic_definition(self, raw_service_definition):
        return raw_service_definition is None

    def __is_alias(self, raw_service_definition):
        return raw_service_definition[:1] == "@"
