from box import Box
from Injecta.Parameter.PlaceholderReplacer import PlaceholderReplacer
from Injecta.Config.ConfigMerger import ConfigMerger

class ParametersParser:

    def __init__(self):
        self.__placeholderReplacer = PlaceholderReplacer()
        self.__configMerger = ConfigMerger()

    def parse(self, rawParameters: dict, customParameters: dict = None):
        if customParameters is not None:
            rawParameters = self.__configMerger.merge(rawParameters, customParameters)

        parameters = self.__placeholderReplacer.replace(rawParameters)

        return Box(parameters)
