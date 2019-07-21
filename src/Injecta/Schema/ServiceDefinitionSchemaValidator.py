from Injecta.Schema.SchemaValidationException import SchemaValidationException

class ServiceDefinitionSchemaValidator:

    ALLOWED_ATTRIBUTES = ['class', 'arguments', 'tags', 'autowire', 'import']

    def validate(self, serviceName, rawServiceDefinition):
        if self.__isBasicDefinition(rawServiceDefinition):
            return
        elif isinstance(rawServiceDefinition, list):
            raise SchemaValidationException('Arguments of service "{}" must be defined in the "arguments" key'.format(serviceName))
        elif isinstance(rawServiceDefinition, dict) is False:
            raise SchemaValidationException('Service "{}" not properly defined'.format(serviceName))

        unexpectedAttributes = set(rawServiceDefinition.keys()) - set(ServiceDefinitionSchemaValidator.ALLOWED_ATTRIBUTES)

        if len(unexpectedAttributes) > 0:
            raise SchemaValidationException('Unexpected attributes ({}) for service "{}"'.format(', '.join(unexpectedAttributes), serviceName))

        if 'arguments' in rawServiceDefinition:
            if isinstance(rawServiceDefinition['arguments'], list) is False:
                raise SchemaValidationException('Arguments of service "{}" must be defined as list'.format(serviceName))

        if 'tags' in rawServiceDefinition:
            if isinstance(rawServiceDefinition['tags'], list) is False:
                raise SchemaValidationException('Tags of service "{}" must be defined as list'.format(serviceName))

        if 'autowire' in rawServiceDefinition:
            if isinstance(rawServiceDefinition['autowire'], bool) is False:
                raise SchemaValidationException('Attribute "autowire" of service "{}" must be True or False'.format(serviceName))

        return True

    def __isBasicDefinition(self, rawServiceDefinition):
        return rawServiceDefinition is None
