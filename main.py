from bmi import bmi_print
from utils import _input


if __name__ == '__main__':
    mass = _input('mass (kg) = ')
    height = _input('height (cm) = ')
    bmi_print(mass, height)
