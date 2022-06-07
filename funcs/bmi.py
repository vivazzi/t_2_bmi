import math


def get_bmi(mass: float, height: float) -> float:
    """
    :param mass: in kg
    :param height: in cm
    :return: body mass index
    """
    return mass / ((height / 100) ** 2)


def get_mass_by_bmi(height: float, bmi: float) -> float:
    """
    :param height: in cm
    :param bmi: body mass index
    :return: mass (in kg) by body mass index
    """
    return ((height / 100) ** 2) * bmi


def get_bmi_data(mass: float, height: float) -> [str, float]:
    """
    :param mass: in kg
    :param height: in cm
    :return: result and deviation from the norm
    """
    bmi = get_bmi(mass, height)

    normal_start = 18.5
    normal_end = 25

    if bmi < 18.5:
        return 'Underweight', get_mass_by_bmi(height, normal_start) - mass

    elif 25 < bmi < 30:
        return 'Overweight', mass - get_mass_by_bmi(height, normal_end)

    elif bmi >= 30:
        return 'Obesity', mass - get_mass_by_bmi(height, normal_end)

    return 'Normal', 0


def bmi_str(mass: float, height: float) -> str:
    """
    :param mass: in kg
    :param height: in cm
    :return: human representation of bmi result with deviation from the norm if there is
    """
    result, deviation = get_bmi_data(mass, height)

    if deviation == 0:
        return result

    return f'{result} {math.ceil(deviation)} kg'
