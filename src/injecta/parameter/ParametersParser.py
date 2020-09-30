from box import Box
from injecta.parameter.PlaceholderFiller import PlaceholderFiller
from injecta.config.ConfigMerger import ConfigMerger

class ParametersParser:

    def __init__(self):
        self.__placeholderFiller = PlaceholderFiller()
        self.__configMerger = ConfigMerger()

    def parse(self, rawParameters: dict, customParameters: dict = None):
        if customParameters is not None:
            rawParameters = self.__configMerger.merge(rawParameters, customParameters)

        parameters = self.__placeholderFiller.fill(rawParameters)

        return Box(parameters)
