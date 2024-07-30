#!/usr/bin/env python3

def access_nested_map(nested_map, path):
    """
    Access a nested dictionary with a sequence of keys.
    :param nested_map: The nested dictionary
    :param path: A sequence of keys to access the value.
    :return: The value located at the specified path.
    :raises KeyError: If any key in the path is not found.
    """

    current = nested_map
    for key in path:
        if key in current:
            current = current[key]
        else:
            raise KeyError(f"Key {key} not found in the map")
    return current
# Example usage
if __name__ == '__main__':
    nested_dict = {
            'a': {
                'b': {
                    'c': 'Value'
                    }
            }
    }

    path = ['a', 'b', 'c']
    value = access_nested_map(nested_dict, path)
    print(value)
