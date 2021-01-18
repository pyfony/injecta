def split(placeholder: str):
    parts = placeholder.split('.')

    output = []
    buffer = []

    for part in parts:
        if part[0] == '"':
            buffer.append(part[1:])
        elif part[-1] == '"':
            buffer.append(part[:-1])
            output.append('.'.join(buffer))
            buffer = []
        elif buffer:
            buffer.append(part)
        else:
            output.append(part)

    return output
