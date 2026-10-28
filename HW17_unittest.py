import HW17_calc
import unittest

class MyTestSuite(unittest.TestCase):
# сложение
    def test_plus(self):
        result = HW17_calc.plus(5,4)
        self.assertEqual( 9, result)

    def test_plus_negative_result(self):
        result = HW17_calc.plus(-100, 20)
        self.assertEqual(-80, result)

    def test_plus_float_result(self):
        result = HW17_calc.plus(1, 0.5)
        self.assertEqual(1.5, result)
# вычитание
    def test_minus(self):
        result = HW17_calc.minus(10,20)
        self.assertEqual( -10, result)

    def test_minus_negative_result(self):
        result = HW17_calc.minus(-100, 20)
        self.assertEqual(-120, result)

    def test_minus_float_result(self):
        result = HW17_calc.minus(1, 0.5)
        self.assertEqual(0.5, result)
# умножение
    def test_multiply(self):
        result = HW17_calc.multiply(10,20)
        self.assertEqual(200, result)

    def test_multiply_negative_result(self):
        result = HW17_calc.multiply(-100, 20)
        self.assertEqual(-2000, result)

    def test_multiply_float_result(self):
        result = HW17_calc.multiply(1, 0.5)
        self.assertEqual(0.5, result)
# деление
    def test_divide(self):
        result = HW17_calc.divide(15,3)
        self.assertEqual(5, result)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            HW17_calc.divide(1, 0)

    def test_divide_negative_result(self):
        result = HW17_calc.divide(-100, 20)
        self.assertEqual(-5, result)

    def test_divide_float_result(self):
        result = HW17_calc.divide(1, 2)
        self.assertEqual(0.5, result)
# возведение в степень
    def test_power(self):
        result = HW17_calc.power(5,4)
        self.assertEqual(625, result)

    def test_power_negative_result(self):
        result = HW17_calc.power(-2, 3)
        self.assertEqual(-8, result)

    def test_power_float_result(self):
        result = HW17_calc.power(4, 0.5)
        self.assertEqual(2.0, result)
