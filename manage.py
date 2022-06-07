import sys

from utils import import_string

AVAILABLE_RUNS = {
    'funcs_bmi': 'funcs.main.run',
    'class_bmi': 'classes.main.run',
}


if __name__ == '__main__':
    try:
        import_string(AVAILABLE_RUNS[sys.argv[1]])()
    except (IndexError, KeyError):
        print(f'Use available arguments:\npipenv run python manage.py [{"|".join(AVAILABLE_RUNS.keys())}]')
