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
        self.equal.click()
        return int(self.result.text)

    def minus(self, n1, n2):
        self._tap_number(n1)
        self.op_minus.click()
        self._tap_number(n2)
        self.equal.click()
        return int(self.result.text)

    def multiply(self, n1, n2):
        self._tap_number(n1)
        self.op_multiply.click()
        self._tap_number(n2)
        self.equal.click()
        return int(self.result.text)

    def divide(self, n1, n2):
        self._tap_number(n1)
        self.op_divide.click()
        self._tap_number(n2)
        self.equal.click()
        return self.result.text
