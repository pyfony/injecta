from injecta.parameter.allPlaceholdersReplacer import replaceAllPlaceholders, findAllPlaceholders

class PlaceholderFiller:

    __appConfigWithResolvers = {}

    def fill(self, appConfig: dict):
        self.__appConfigWithResolvers = {k: self.__resolvePlaceholders(v, k) for k, v in appConfig.items()}

        return {k: self.__resolveFinalValues(v) for k, v in self.__appConfigWithResolvers.items()}

    def __resolvePlaceholders(self, value, path: str):
        if isinstance(value, dict):
            return {k: self.__resolvePlaceholders(v, path + '.' + k) for k, v in value.items()}

        if isinstance(value, list):
            return list(map(lambda value: self.__resolvePlaceholders(value, path), value))

        if isinstance(value, str):
            matches = findAllPlaceholders(value)

            if not matches:
                return value

            return lambda: replaceAllPlaceholders(value, matches, self.__appConfigWithResolvers, path)

        return value

    def __resolveFinalValues(self, value):
        if isinstance(value, dict):
            return {k: self.__resolveFinalValues(v) for k, v in value.items()}

        if isinstance(value, list):
            return list(map(self.__resolveFinalValues, value))

        if callable(value):
            return self.__resolveFinalValues(value())

        return value
