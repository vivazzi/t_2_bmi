import math


class BMI:
    def __init__(self, mass: float, height: float):
        self.mass = mass
        self.height = height

    def get_bmi(self) -> float:
        return self.mass / ((self.height / 100) ** 2)

    def get_mass_by_bmi(self, bmi: float) -> float:
        return ((self.height / 100) ** 2) * bmi

    def get_bmi_data(self) -> [str, float]:
        """
        :param mass: kg
        :param height: cm
        :return: result and deviation from the norm
        """
        bmi = self.get_bmi()

        normal_start_bmi = 18.5
        normal_end_bmi = 25

        if bmi < 18.5:
            return 'Underweight', self.get_mass_by_bmi(normal_start_bmi) - self.mass

        elif 25 < bmi < 30:
            return 'Overweight', self.mass - self.get_mass_by_bmi(normal_end_bmi)

        elif bmi >= 30:
            return 'Obesity', self.mass - self.get_mass_by_bmi(normal_end_bmi)

        else:
            return 'Normal', 0

    def result_str(self) -> str:
        result, deviation = self.get_bmi_data()

        if deviation == 0:
            return result

        return f'{result} {math.ceil(deviation)} kg'

    def print_result(self) -> None:
        print(self.result_str())
