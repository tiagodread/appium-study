import unittest
from pageobjects.calculator import Calc
from webdriver.webdriver import Driver


class CalcTests(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.calc = Calc(self.driver.instance)

    def test_sum(self):
        result = int(self.calc.sum(1, 1))
        assert result == 2

    def test_minus(self):
        result = int(self.calc.minus(5, 3))
        assert result == 2

    def test_multiply(self):
        result = int(self.calc.multiply(9, 9))
        assert result == 81

    def test_divide(self):
        result = int(self.calc.divide(8, 4))
        assert result == 2

    def test_divide_nan(self):
        result = self.calc.divide(4, 0)
        assert "Can't divide by 0" in result

    def tearDown(self):
        self.driver.instance.quit()
