# pylint: disable = too-many-return-statements
from injecta.service.argument.DictArgument import DictArgument
from injecta.service.argument.ListArgument import ListArgument
from injecta.service.argument.TaggedAliasedServiceArgument import TaggedAliasedServiceArgument
from injecta.service.argument.ServiceArgument import ServiceArgument
from injecta.service.argument.PrimitiveArgument import PrimitiveArgument
from injecta.config.ConfigLoader import TaggedServices, TaggedAliasedService
from injecta.service.argument.TaggedServicesArgument import TaggedServicesArgument

class ArgumentParser:

    def parse(self, argument, name=None):
        if isinstance(argument, str):
            if argument[0:1] == '@':
                return ServiceArgument(argument[1:], name)

            return PrimitiveArgument(argument, name)

        if isinstance(argument, TaggedServices):
            return TaggedServicesArgument(argument.val, name)

        if isinstance(argument, TaggedAliasedService):
            return TaggedAliasedServiceArgument(argument.tagName, argument.tagAlias, name)

        if isinstance(argument, (int, bool)):
            return PrimitiveArgument(argument, name)

        if isinstance(argument, list):
            return ListArgument(list(map(self.parse, argument)), name)

        if isinstance(argument, dict):
            return DictArgument({k: self.parse(v) for k, v in argument.items()}, name)

        raise Exception('Unexpected argument type: {}'.format(type(argument)))
