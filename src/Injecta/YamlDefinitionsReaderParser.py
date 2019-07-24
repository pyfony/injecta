from Injecta.YamlDefinitionsParser import YamlDefinitionsParser

class YamlDefinitionsReaderParser:

    def __init__(self):
        self.__yamlDefinitionsParser = YamlDefinitionsParser()

    def readAndParse(self, servicesConfigPath: str):
        definitionsString = self.__read(servicesConfigPath)
        
        return self.__yamlDefinitionsParser.parse(definitionsString)

    def __read(self, servicesConfigPath):
        with open(servicesConfigPath, 'r', encoding='utf-8') as f:
            yamlDefinitionsString = f.read()
            f.close()

        return yamlDefinitionsString
