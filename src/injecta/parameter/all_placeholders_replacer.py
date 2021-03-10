import re
from functools import reduce
import operator
import os
from injecta.parameter.placeholder_replacer import replace_placeholder
from injecta.parameter import placeholder_splitter


def find_all_placeholders(value: str):
    return re.findall(r'%(["a-zA-Z0-9_.()-]+)%', value)


def replace_all_placeholders(original_input: str, placeholders: list, final_values: dict, path: str):
    for placeholder in placeholders:
        if placeholder[:4] == "env(":
            env_variable_name = placeholder[4:-1]

            if env_variable_name not in os.environ:
                raise Exception(f'Undefined environment variable "{env_variable_name}" used in {path}')

            original_input = replace_placeholder(original_input, placeholder, os.environ[env_variable_name], path)
        else:
            try:
                final_value = reduce(operator.getitem, placeholder_splitter.split(placeholder), final_values)
            except KeyError:
                raise Exception(f'Parameter "{placeholder}" used in {path} not found')

            final_value_resolved = final_value() if callable(final_value) else final_value
            original_input = replace_placeholder(original_input, placeholder, final_value_resolved, path)

    return original_input
