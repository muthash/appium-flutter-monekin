from appium.webdriver.common.appiumby import AppiumBy


class NativeFinders:
    def __init__(self, driver):
        self._driver = driver

    def find_element_by_id(self, resource_id):
        return self._driver.find_element(AppiumBy.ID, resource_id)

    def find_element_by_accessibility_id(self, accessibility_id):
        return self._driver.find_element(AppiumBy.ACCESSIBILITY_ID, accessibility_id)

    def find_element_by_name(self, name):
        return self._driver.find_element(AppiumBy.NAME, name)

    def find_element_by_xpath(self, xpath):
        return self._driver.find_element(AppiumBy.XPATH, xpath)

    def find_element_by_class_name(self, class_name):
        return self._driver.find_element(AppiumBy.CLASS_NAME, class_name)
