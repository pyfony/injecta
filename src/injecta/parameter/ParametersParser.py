from box import Box
from injecta.parameter.PlaceholderReplacer import PlaceholderReplacer
from injecta.config.ConfigMerger import ConfigMerger

class ParametersParser:

    def __init__(self):
        self.__placeholderReplacer = PlaceholderReplacer()
        self.__configMerger = ConfigMerger()

    def parse(self, rawParameters: dict, customParameters: dict = None):
        if customParameters is not None:
            rawParameters = self.__configMerger.merge(rawParameters, customParameters)

        parameters = self.__placeholderReplacer.replace(rawParameters)

        return Box(parameters)
