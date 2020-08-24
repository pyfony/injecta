from functools import reduce
import operator
import re
import os

class PlaceholderReplacer:

    __appConfigWithResolvers = {}

    def replace(self, appConfig: dict):
        self.__appConfigWithResolvers = {k: self.__resolvePlaceholders(v, k) for k, v in appConfig.items()}

        return {k: self.__resolveFinalValues(v) for k, v in self.__appConfigWithResolvers.items()}

    def __resolvePlaceholders(self, value, path: str):
        if isinstance(value, dict):
            return {k: self.__resolvePlaceholders(v, path + '.' + k) for k, v in value.items()}

        if isinstance(value, list):
            return list(map(lambda value: self.__resolvePlaceholders(value, path), value))

        if isinstance(value, str):
            matches = re.findall(r'%([a-zA-Z0-9_.()-]+)%', value)

            if not matches:
                return value

            return self.__replaceAllPlaceholders(matches, value, path)

        return value

    def __replaceAllPlaceholders(self, placeholders: list, value, path: str):
        def resolver():
            output = value

            for placeholder in placeholders:
                if placeholder[:4] == 'env(':
                    envVariableName = placeholder[4:-1]

                    if envVariableName not in os.environ:
                        raise Exception(f'Undefined environment variable "{envVariableName}" used in {path}')

                    output = self.__replacePlaceholderWithValue(output, placeholder, os.environ[envVariableName], path)
                else:
                    try:
                        finalValue = reduce(operator.getitem, placeholder.split('.'), self.__appConfigWithResolvers)
                    except KeyError:
                        raise Exception(f'Parameter "{placeholder}" used in {path} not found')

                    finalValueResolved = finalValue() if callable(finalValue) else finalValue
                    output = self.__replacePlaceholderWithValue(output, placeholder, finalValueResolved, path)

            return output

        return resolver

    def __replacePlaceholderWithValue(self, output, placeholder: str, finalValueResolved, path: str):
        if isinstance(finalValueResolved, str):
            return output.replace('%{}%'.format(placeholder), finalValueResolved)

        if isinstance(finalValueResolved, int):
            if output == ('%' + placeholder + '%'):
                return finalValueResolved

            return output.replace('%{}%'.format(placeholder), str(finalValueResolved))

        if isinstance(finalValueResolved, (bool, dict, list)):
            if output != ('%' + placeholder + '%'):
                raise Exception(f'Merging {type(finalValueResolved)} parameters with other variable types is not allowed in {path}')

            return finalValueResolved

        if finalValueResolved is None:
            if output != ('%' + placeholder + '%'):
                raise Exception(f'Merging None value with other variable types is not allowed in {path}')

            return finalValueResolved

        raise Exception(f'Unexpected type: {type(finalValueResolved)} for {placeholder} in {path}')

    def __resolveFinalValues(self, value):
        if isinstance(value, dict):
            return {k: self.__resolveFinalValues(v) for k, v in value.items()}

        if isinstance(value, list):
            return list(map(self.__resolveFinalValues, value))

        if callable(value):
            return self.__resolveFinalValues(value())

        return value
