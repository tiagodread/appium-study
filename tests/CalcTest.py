import unittest
from pageobjects.calculator import Calc
from webdriver.webdriver import Driver


class CalcTests(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.calc = Calc(self.driver.instance)

    def test_sum(self):
        result = self.calc.sum(1, 1)
        assert result == 2

