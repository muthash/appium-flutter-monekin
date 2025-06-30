import os
import logging

from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.options.common.base import AppiumOptions
from appium import webdriver

from setup_utilities.data_reader import DataReader


class DriverFactory:
    """
    This class contains the reusable methods for getting the driver instances
    """

    log = logging.getLogger(__name__)
    logging.basicConfig(filename="myapp.log", level=logging.INFO)
    data_reader = DataReader()

    def __init__(self, platform):
        self.platform = platform
        self.cur_path = os.path.abspath(os.path.dirname(__file__))
        self.local_appium_server = "http://localhost:4723"

    def get_driver_instance(self):
        desired_caps = self.data_reader.get_desired_caps(self.platform)
        app_location = os.path.join(self.cur_path, r"../apps/", desired_caps["app"])
        
        desired_caps["app"] = app_location

        options_caps = {
            "flutter_android": AppiumOptions().load_capabilities(desired_caps),
            "flutter_ios": AppiumOptions().load_capabilities(desired_caps),
            "native_android": UiAutomator2Options().load_capabilities(desired_caps),
            "native_ios": XCUITestOptions().load_capabilities(desired_caps),
        }

        return webdriver.Remote(
            self.local_appium_server, options=options_caps[self.platform]
        )
