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
        elif isinstance(value, list):
            return list(map(lambda listItem: self.__resolvePlaceholders(listItem), value))
        elif isinstance(value, str):
            matches = re.findall(r'%([^%]+)%', value)

            if len(matches) == 0:
                return value
            else:
                return self.__replaceAllPlaceholders(matches, value)
        else:
            return value

    def __replaceAllPlaceholders(self, placeholders: list, value):
        def resolver():
            output = value

            for placeholder in placeholders:
                if placeholder[:4] == 'env(':
                    envVariableName = placeholder[4:-1]

                    if envVariableName not in os.environ:
                        raise Exception('Environment variable "{}" not defined'.format(envVariableName))

                    output = self.__replacePlaceholder(output, placeholder, os.environ[envVariableName])
                else:
                    try:
                        finalValue = reduce(operator.getitem, placeholder.split('.'), self.__appConfigWithResolvers)
                    except KeyError:
                        raise Exception('Parameter "{}" not found'.format(placeholder))

                    finalValueResolved = finalValue() if callable(finalValue) else finalValue
                    output = self.__replacePlaceholder(output, placeholder, finalValueResolved)

            return output

        return resolver

    def __replacePlaceholder(self, output, placeholder: str, finalValueResolved):
        if isinstance(finalValueResolved, str):
            return output.replace('%{}%'.format(placeholder), finalValueResolved)
        elif isinstance(finalValueResolved, int):
            if output == ('%' + placeholder + '%'):
                return finalValueResolved
            else:
                return output.replace('%{}%'.format(placeholder), str(finalValueResolved))
        elif isinstance(finalValueResolved, bool):
            if output == ('%' + placeholder + '%'):
                return finalValueResolved
            else:
                raise Exception('Merging boolean parameters with other variable types is not allowed')
        else:
            raise Exception('Unexpected type: {}'.format(type(finalValueResolved)))

    def __resolveFinalValues(self, value):
        if isinstance(value, dict):
            return {k: self.__resolveFinalValues(v) for k, v in value.items()}
        elif isinstance(value, list):
            return list(map(lambda listItem: self.__resolveFinalValues(listItem), value))
        elif callable(value):
            return value()
        else:
            return value
