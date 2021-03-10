from typing import Optional
from injecta.service.argument.ArgumentInterface import ArgumentInterface
from injecta.service.class_.InspectedArgument import InspectedArgument


class ResolvedArgument:
    def __init__(
        self,
        name: str,
        argument: Optional[ArgumentInterface],  # nullable in case of services to be autowired
        inspected_argument: Optional[InspectedArgument],
    ):
        self.__name = name
        self.__argument_history = [{"argument": argument, "description": "config definition"}]
        self.__inspected_argument = inspected_argument

    @property
    def name(self):
        return self.__name

    @property
    def argument(self):
        return self.__argument_history[-1]["argument"]

    def modify_argument(self, argument: ArgumentInterface, change_description: str):
        self.__argument_history.append({"argument": argument, "description": change_description})

    @property
    def inspected_argument(self):
        return self.__inspected_argument
