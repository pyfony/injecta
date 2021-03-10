from injecta.parameter.all_placeholders_replacer import replace_all_placeholders, find_all_placeholders


class PlaceholderFiller:

    __app_config_with_resolvers = {}

    def fill(self, app_config: dict):
        self.__app_config_with_resolvers = {k: self.__resolve_placeholders(v, k) for k, v in app_config.items()}

        return {k: self.__resolve_final_values(v) for k, v in self.__app_config_with_resolvers.items()}

    def __resolve_placeholders(self, value, path: str):
        if isinstance(value, dict):
            return {k: self.__resolve_placeholders(v, path + "." + k) for k, v in value.items()}

        if isinstance(value, list):
            return list(map(lambda value: self.__resolve_placeholders(value, path), value))

        if isinstance(value, str):
            matches = find_all_placeholders(value)

            if not matches:
                return value

            return lambda: replace_all_placeholders(value, matches, self.__app_config_with_resolvers, path)

        return value

    def __resolve_final_values(self, value):
        if isinstance(value, dict):
            return {k: self.__resolve_final_values(v) for k, v in value.items()}

        if isinstance(value, list):
            return list(map(self.__resolve_final_values, value))

        if callable(value):
            return self.__resolve_final_values(value())

        return value
