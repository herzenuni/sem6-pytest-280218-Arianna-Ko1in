def solve_dict(keys: list, values: list)->dict:
    result = {}
    for i, key in enumerate(keys):
        try:
            result[key] = values[i]
        except IndexError:
            result[key] = None

    return result
