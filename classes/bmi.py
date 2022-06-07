import math


class BMI:
    def __init__(self, mass: float, height: float):
        """
        :param mass: in kg
        :param height: in cm
        """
        self.mass = mass
        self.height = height

    def get_bmi(self) -> float:
        """
        :return: body mass index
        """
        return self.mass / ((self.height / 100) ** 2)

    def get_mass_by_bmi(self, bmi: float) -> float:
        """
        :param bmi: body mass index
        :return: mass (in kg) by body mass index
        """
        return ((self.height / 100) ** 2) * bmi

    def get_bmi_data(self) -> [str, float]:
        """
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

    def result(self) -> str:
        """
        :return: human representation of bmi result with deviation from the norm if there is
        """
        result, deviation = self.get_bmi_data()

        if deviation == 0:
            return result

        return f'{result} {math.ceil(deviation)} kg'
