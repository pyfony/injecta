from typing import Optional
from injecta.service.argument.ArgumentInterface import ArgumentInterface
from injecta.service.class_.InspectedArgument import InspectedArgument

class ResolvedArgument:

    def __init__(
        self,
        name: str,
        argument: Optional[ArgumentInterface], # nullable in case of services to be autowired
        inspectedArgument: Optional[InspectedArgument],
    ):
        self.__name = name
        self.__argumentHistory = [{'argument': argument, 'description': 'config definition'}]
        self.__inspectedArgument = inspectedArgument

    @property
    def name(self):
        return self.__name

    @property
    def argument(self):
        return self.__argumentHistory[-1]['argument']

    def modifyArgument(self, argument: ArgumentInterface, changeDescription: str):
        self.__argumentHistory.append({'argument': argument, 'description': changeDescription})

    @property
    def inspectedArgument(self):
        return self.__inspectedArgument
