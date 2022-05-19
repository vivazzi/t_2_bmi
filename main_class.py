from bmi_class import BMI
from utils import _input


if __name__ == '__main__':
    mass = _input('mass (kg) = ')
    height = _input('height (cm) = ')
    BMI(mass, height).print_result()
