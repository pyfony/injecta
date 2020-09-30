def replacePlaceholder(originalInput, placeholder: str, finalValueResolved, path: str):
    if isinstance(finalValueResolved, str):
        return originalInput.replace(f'%{placeholder}%', finalValueResolved)

    if isinstance(finalValueResolved, int):
        if originalInput == f'%{placeholder}%':
            return finalValueResolved

        return originalInput.replace(f'%{placeholder}%', str(finalValueResolved))

    if isinstance(finalValueResolved, (bool, dict, list)):
        if originalInput != f'%{placeholder}%':
            raise Exception(f'Merging {finalValueResolved.__class__.__name__} parameters with other variable types is not allowed in {path}')

        return finalValueResolved

    if finalValueResolved is None:
        if originalInput != f'%{placeholder}%':
            raise Exception(f'Merging None value with other variable types is not allowed in {path}')

        return finalValueResolved

    raise Exception(f'Unexpected type: {type(finalValueResolved)} for {placeholder} in {path}')
