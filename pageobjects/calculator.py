from webdriver.webdriver import Driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy


class Calc:
    def __init__(self, driver):
        self.driver = driver
        self.op_plus = driver.find_element(by=AppiumBy.ID, value="com.android.calculator2:id/op_add")
        self.op_minus = driver.find_element(by=AppiumBy.ID, value="com.android.calculator2:id/op_sub")
        self.op_multiply = driver.find_element(by=AppiumBy.ID, value="com.android.calculator2:id/op_mul")
        self.op_divide = driver.find_element(by=AppiumBy.ID, value="com.android.calculator2:id/op_div")

        self.equal = driver.find_element(by=AppiumBy.ID, value="com.android.calculator2:id/eq")
        self.result = driver.find_element(by=AppiumBy.ID, value="com.android.calculator2:id/result")

    def _tap_number(self, number):
        _number = str(number)
        self.driver.find_element(by=AppiumBy.ID, value="com.android.calculator2:id/digit_" + _number).click()

    def sum(self, n1, n2):
        self._tap_number(n1)
        self.op_plus.click()
        self._tap_number(n2)
        return int(self.result.text)
