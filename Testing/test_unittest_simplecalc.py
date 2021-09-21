from simplecalc import SimpleCalc
import unittest


class CalcTest(unittest.TestCase):

    calc = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 4), 6)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(6, 4), 2)

    # def test_multiply(self):
    #     self.assertEqual(self.calc.multiply(2, 4), 8)
    #
    # def test_divide(self):
    #     self.assertEqual(self.calc.divide(6, 2), 3)
