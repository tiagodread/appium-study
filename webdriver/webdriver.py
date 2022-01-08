from appium import webdriver


class Driver:
    def __init__(self):
        desired_cap = {
            "platformName": "Android",
            "appium:deviceName": "emulator-5554",
            "appium:avd": "pi4",
            "appium:appPackage": "com.android.calculator2",
            "appium:appActivity": "com.android.calculator2.Calculator"
        }

        self.instance = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
