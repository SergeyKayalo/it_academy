import operator
import random

import HW17_calc
import unittest


def _random_number(allow_float=True):
    if allow_float and random.random() < 0.5:
        return round(random.uniform(-9999999, 9999999), 2)
    return random.randint(-9999999, 9999999)

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
        result = HW17_calc.multiply(-100.0, 20)
        self.assertEqual(-2000, result)

    def test_multiply_float_result(self):
        result = HW17_calc.multiply(1, 0.5)
        self.assertEqual(0.5, result)

    def test_multiply_bigint_result(self):
        result = HW17_calc.multiply(999999999999999999999999999999, 999999999999999999999999999999)
        self.assertEqual(999999999999999999999999999998000000000000000000000000000001, result)

    def test_multiply_bigfloat_result(self):
        result = HW17_calc.multiply(999999999999999999999999999999.0, 999999999999999999999999999999.0)
        self.assertAlmostEqual(999999999999999999999999999998000000000000000000000000000001.0, result, places=6)

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

    def test_power_bigfloat_result(self):
        with self.assertRaises(OverflowError):
            HW17_calc.power(9999, 99999.0)

    def test_power_devision_zero(self):
        with self.assertRaises(ZeroDivisionError):
            HW17_calc.power(0, -6)
# рандомные тесты


    def test_random_operations(self):
        OPERATIONS = [
            ("+", operator.add),
            ("-", operator.sub),
            ("*", operator.mul),
            ("/", operator.truediv),
            ("^", operator.pow)
        ]
        for op, ref in OPERATIONS:
            for _ in range(50):
                if op == "^":
                    a = random.randint(-20, 20)
                    b = random.randint(-6, 6)
                else:
                    a = _random_number()
                    b = _random_number()

                # фильтры ПОСЛЕ генерации
                if op == "/" and b == 0:
                    continue
                if op == "^" and a == 0 and b < 0:
                    continue

                with self.subTest(op=op, a=a, b=b):
                    self.assertAlmostEqual(
                        ref(a, b),
                        HW17_calc.arithmetic(a, op, b),
                        places=6,
                        msg=f"op={op}, a={a}, b={b}"
                    )