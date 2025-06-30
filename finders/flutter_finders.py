import logging


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (
    StaleElementReferenceException,
    WebDriverException,
)

log = logging.getLogger(__name__)


class FlutterFinder:
    def __init__(self, driver):
        self._driver = driver

    def by_value_key(self, key):
        return self._driver.execute_script(
            "flutter:findElement", {"finderType": "byValueKey", "keyValueString": key}
        )

    def by_text(self, text):
        return self._driver.execute_script(
            "flutter:findElement", {"finderType": "byText", "text": text}
        )

    def by_tooltip(self, tooltip):
        return self._driver.execute_script(
            "flutter:findElement", {"finderType": "byTooltip", "text": tooltip}
        )

    def by_type(self, widget_type):
        return self._driver.execute_script(
            "flutter:findElement", {"finderType": "byType", "type": widget_type}
        )

    def descendant(self, of_key, matching_type, match_root=True):
        return self._driver.execute_script(
            "flutter:findElement",
            {
                "finderType": "descendant",
                "matchRoot": match_root,
                "of": {"finderType": "byValueKey", "keyValueString": of_key},
                "matching": {"finderType": "byType", "type": matching_type},
            },
        )


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

    def is_element_present(
        self, locator_properties, locator_type="id", max_time_out=10
    ):
        """
        This method checks for presence of element & return the bollean value
        :param locator_properties: it takes locator string as parameter
        :param locator_type: it takes locator type as parameter
        :param max_time_out: this is the maximum time to wait for particular element
        """
        try:
            WebDriverWait(
                self._driver,
                max_time_out,
                ignored_exceptions=[StaleElementReferenceException],
            ).until(
                EC.presence_of_element_located(
                    (self.get_locator_type(locator_type), locator_properties)
                )
            )
            return True
        except WebDriverException:
            log.error(
                "Element is not present with locator_properties: "
                + locator_properties
                + " and locator_type: "
                + locator_type
            )
            return False

    def get_text(self, element):
        return self._driver.execute_script("flutter:getText", {"element": element})

    def enter_text(self, element, text):
        return self._driver.execute_script(
            "flutter:enterText", {"element": element, "text": text}
        )

    def tap(self, element):
        return self._driver.execute_script("flutter:tap", {"element": element})

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
