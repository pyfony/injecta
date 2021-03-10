def replace_placeholder(original_input, placeholder: str, final_value_resolved, path: str):
    if isinstance(final_value_resolved, str):
        return original_input.replace(f"%{placeholder}%", final_value_resolved)

    if isinstance(final_value_resolved, int):
        if original_input == f"%{placeholder}%":
            return final_value_resolved

        return original_input.replace(f"%{placeholder}%", str(final_value_resolved))

    if isinstance(final_value_resolved, (bool, dict, list)):
        if original_input != f"%{placeholder}%":
            raise Exception(
                f"Merging {final_value_resolved.__class__.__name__} parameters with other variable types is not allowed in {path}"
            )

        return final_value_resolved

    if final_value_resolved is None:
        if original_input != f"%{placeholder}%":
            raise Exception(f"Merging None value with other variable types is not allowed in {path}")

        return final_value_resolved

    raise Exception(f"Unexpected type: {type(final_value_resolved)} for {placeholder} in {path}")
