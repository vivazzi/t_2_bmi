from .bmi import BMI
from utils import _input


def run():
    mass = _input('mass (kg) = ')
    height = _input('height (cm) = ')
    print(BMI(mass, height).result())
