from functools import reduce
import operator
import re
import os

class PlaceholderReplacer:

    __appConfigWithResolvers = {}

    def replace(self, appConfig: dict):
        self.__appConfigWithResolvers = self.__resolvePlaceholders(appConfig.items())

        return self.__resolveFinalValues(self.__appConfigWithResolvers.items())

    def __resolvePlaceholders(self, iterable):
        output = {}

        for key, value in iterable:
            if isinstance(value, dict):
                output[key] = self.__resolvePlaceholders(value.items())
            elif isinstance(value, list):
                output[key] = list(map(lambda listItem: self.__resolvePlaceholders(enumerate(listItem)), value))
            elif isinstance(value, str):
                matches = re.findall(r'%([^%]+)%', value)

                if len(matches) == 0:
                    output[key] = value
                else:
                    output[key] = self.__replaceAllPlaceholders(matches, value)
            else:
                output[key] = value

        return output

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

    def __resolveFinalValues(self, iterable):
        output = {}

        for key, value in iterable:
            if isinstance(value, dict):
                output[key] = self.__resolveFinalValues(value.items())
            elif isinstance(value, list):
                output[key] = list(map(lambda listItem: self.__resolveFinalValues(enumerate(listItem)), value))
            elif callable(value):
                output[key] = value()
            else:
                output[key] = value

        return output
