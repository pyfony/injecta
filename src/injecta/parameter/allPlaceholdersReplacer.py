import re
from functools import reduce
import operator
import os
from injecta.parameter.placeholderReplacer import replacePlaceholder
from injecta.parameter import placeholderSplitter

def findAllPlaceholders(value: str):
    return re.findall(r'%(["a-zA-Z0-9_.()-]+)%', value)

def replaceAllPlaceholders(originalInput: str, placeholders: list, finalValues: dict, path: str):
    for placeholder in placeholders:
        if placeholder[:4] == 'env(':
            envVariableName = placeholder[4:-1]

            if envVariableName not in os.environ:
                raise Exception(f'Undefined environment variable "{envVariableName}" used in {path}')

            originalInput = replacePlaceholder(originalInput, placeholder, os.environ[envVariableName], path)
        else:
            try:
                finalValue = reduce(operator.getitem, placeholderSplitter.split(placeholder), finalValues)
            except KeyError:
                raise Exception(f'Parameter "{placeholder}" used in {path} not found')

            finalValueResolved = finalValue() if callable(finalValue) else finalValue
            originalInput = replacePlaceholder(originalInput, placeholder, finalValueResolved, path)

    return originalInput
