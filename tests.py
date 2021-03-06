import unittest

from funcs.bmi import bmi_str
from classes.bmi import BMI


class TestApp(unittest.TestCase):

    def test_bmi(self):
        self.assertEqual(bmi_str(100, 180), 'Obesity 19 kg')
        self.assertEqual(bmi_str(84, 180), 'Overweight 3 kg')
        self.assertEqual(bmi_str(80, 180), 'Normal')
        self.assertEqual(bmi_str(49, 180), 'Underweight 11 kg')

    def test_bmi_class(self):
        self.assertEqual(BMI(100, 180).result(), 'Obesity 19 kg')
        self.assertEqual(BMI(84, 180).result(), 'Overweight 3 kg')
        self.assertEqual(BMI(80, 180).result(), 'Normal')
        self.assertEqual(BMI(49, 180).result(), 'Underweight 11 kg')


if __name__ == '__main__':
    unittest.main()
