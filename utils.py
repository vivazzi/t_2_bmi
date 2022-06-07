import importlib


def _input(mes: str):
    valid = False

    while not valid:
        try:
            v = int(input(mes))

            if v <= 0:
                print('Please input positive number')
                continue

            return v
        except ValueError:
            print('Please only input digits')


def import_string(path: str):
    """
    :param path: Path to function or class
    :return: function or class
    """
    module_name, func_name = path.rsplit('.', 1)
    module = importlib.import_module(module_name)
    return getattr(module, func_name)
