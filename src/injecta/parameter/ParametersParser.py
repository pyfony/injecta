from box import Box
from injecta.parameter.PlaceholderFiller import PlaceholderFiller
from injecta.config.ConfigMerger import ConfigMerger


class ParametersParser:
    def __init__(self):
        self.__placeholder_filler = PlaceholderFiller()
        self.__config_merger = ConfigMerger()

    def parse(self, raw_parameters: dict, custom_parameters: dict = None):
        if custom_parameters is not None:
            raw_parameters = self.__config_merger.merge(raw_parameters, custom_parameters)

        parameters = self.__placeholder_filler.fill(raw_parameters)

        return Box(parameters)
