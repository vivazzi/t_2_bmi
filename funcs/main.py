from .bmi import bmi_str
from utils import _input


def run():
    mass = _input('mass (kg) = ')
    height = _input('height (cm) = ')
    print(bmi_str(mass, height))
