from box import Box
from Injecta.Parameter.PlaceholderReplacer import PlaceholderReplacer

class ParametersParser:

    def __init__(self):
        self.__placeholderReplacer = PlaceholderReplacer()

    def parse(self, rawParameters: dict):
        parameters = self.__placeholderReplacer.replace(rawParameters)

        return Box(parameters)
