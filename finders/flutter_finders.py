import logging

from appium_flutter_finder.flutter_finder import FlutterElement, FlutterFinder
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (
    StaleElementReferenceException,
    WebDriverException,
)

log = logging.getLogger(__name__)


class FlutterFinderWrapper:
    def __init__(self, driver):
        self._driver = driver
        self._finder = FlutterFinder()

    def by_value_key(self, value):
        key_finder = self._finder.by_value_key(value)
        return FlutterElement(self._driver, key_finder)

    def by_text(self, text):
        text_finder = self._finder.by_text(text)
        return FlutterElement(self._driver, text_finder)

    def by_semantics_label(self, label, isRegExp=False):
        label_finder = self._finder.by_semantics_label(label, isRegExp=isRegExp)
        return FlutterElement(self._driver, label_finder)

    def by_tooltip(self, tooltip):
        tooltip_finder = self._finder.by_tooltip(tooltip)
        self._driver.execute_script("flutter:waitFor", tooltip_finder, 100)
        return FlutterElement(self._driver, tooltip_finder)

    def by_type(self, widget_type):
        type_finder = self._finder.by_type(widget_type)
        self._driver.execute_script("flutter:waitFor", type_finder, 100)
        return FlutterElement(self._driver, type_finder)

    def page_back(self):
        back_finder = self._finder.page_back()
        return FlutterElement(self._driver, back_finder)


class FlutterFinderActions:
    def __init__(self, driver):
        self._driver = driver

    def get_locator_type(self, locator_type):
        """
        This method returns the locator type based on the input string
        :param locator_type: it takes locator type as parameter
        """
        locator_type = locator_type.lower()
        if locator_type == "id":
            return "byValueKey"
        elif locator_type == "text":
            return "byText"
        elif locator_type == "tooltip":
            return "byTooltip"
        elif locator_type == "type":
            return "byType"
        else:
            raise ValueError(f"Unsupported locator type: {locator_type}")

    def get_text(self, element):
        return element.text

    def enter_text(self, element, text):
        return element.send_keys(text)

    def click_element(self, element):
        return element.click()

    def assert_text(self, element, expected_text):
        actual = self.get_text(element)
        assert actual == expected_text, f"Expected '{expected_text}', got '{actual}'"

    def assert_text_contains(self, element, expected_substring):
        actual = self.get_text(element)
        assert (
            expected_substring in actual
        ), f"'{expected_substring}' not found in '{actual}'"

    def assert_element_present(self, element):
        assert (
            element is not None
        ), "Expected element to be present but it was not found"
