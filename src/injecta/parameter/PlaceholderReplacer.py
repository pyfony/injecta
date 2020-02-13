from functools import reduce
import operator
import re
import os

class PlaceholderReplacer:

    __appConfigWithResolvers = {}

    def replace(self, appConfig: dict):
        self.__appConfigWithResolvers = {k: self.__resolvePlaceholders(v) for k, v in appConfig.items()}

        return {k: self.__resolveFinalValues(v) for k, v in self.__appConfigWithResolvers.items()}

    def __resolvePlaceholders(self, value):
        if isinstance(value, dict):
            return {k: self.__resolvePlaceholders(v) for k, v in value.items()}

        if isinstance(value, list):
            return list(map(self.__resolvePlaceholders, value))

        if isinstance(value, str):
            matches = re.findall(r'%([a-zA-Z0-9_.()-]+)%', value)

            if not matches:
                return value

            return self.__replaceAllPlaceholders(matches, value)

        return value

    def __replaceAllPlaceholders(self, placeholders: list, value):
        def resolver():
            output = value

            for placeholder in placeholders:
                if placeholder[:4] == 'env(':
                    envVariableName = placeholder[4:-1]

                    if envVariableName not in os.environ:
                        raise Exception('Environment variable "{}" not defined'.format(envVariableName))

                    output = self.__replacePlaceholderWithValue(output, placeholder, os.environ[envVariableName])
                else:
                    try:
                        finalValue = reduce(operator.getitem, placeholder.split('.'), self.__appConfigWithResolvers)
                    except KeyError:
                        raise Exception('parameter "{}" not found'.format(placeholder))

                    finalValueResolved = finalValue() if callable(finalValue) else finalValue
                    output = self.__replacePlaceholderWithValue(output, placeholder, finalValueResolved)

            return output

        return resolver

    def __replacePlaceholderWithValue(self, output, placeholder: str, finalValueResolved):
        if isinstance(finalValueResolved, str):
            return output.replace('%{}%'.format(placeholder), finalValueResolved)

        if isinstance(finalValueResolved, int):
            if output == ('%' + placeholder + '%'):
                return finalValueResolved

            return output.replace('%{}%'.format(placeholder), str(finalValueResolved))

        if isinstance(finalValueResolved, (bool, dict, list)):
            if output != ('%' + placeholder + '%'):
                raise Exception('Merging {} parameters with other variable types is not allowed'.format(type(finalValueResolved)))

            return finalValueResolved

        if finalValueResolved is None:
            if output != ('%' + placeholder + '%'):
                raise Exception('Merging None values with other variable types is not allowed')

            return finalValueResolved

        raise Exception('Unexpected type: {} for {}'.format(type(finalValueResolved), placeholder))

    def __resolveFinalValues(self, value):
        if isinstance(value, dict):
            return {k: self.__resolveFinalValues(v) for k, v in value.items()}

        if isinstance(value, list):
            return list(map(self.__resolveFinalValues, value))

        if callable(value):
            return self.__resolveFinalValues(value())

        return value
