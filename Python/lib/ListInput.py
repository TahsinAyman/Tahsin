def list_input_integer(with_input=' '):
    try:
        return [int(l) for l in input().strip().split(with_input)]
    except ValueError:
        print('Error Input Format')
        return []


def list_input_string(with_input=' '):
    try:
        return [str(l) for l in input().strip().split(with_input)]
    except ValueError:
        print('Error Input Format')
        return []


def list_input_boolean(with_input=' '):
    try:
        return [bool(l) for l in input().strip().split(with_input)]
    except ValueError:
        print('Error Input Format')
        return []


def list_input_float(with_input=' '):
    try:
        return [float(l) for l in input().strip().split(with_input)]
    except ValueError:
        print('Error Input Format')
        return []
