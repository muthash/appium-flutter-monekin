"""This module is used for developing/ accessing data reader utility."""

import json
import os
import traceback


class DataReader:
    """
    This class includes basic reusable data helpers.
    """

    def __init__(self):
        self.cur_path = os.path.abspath(os.path.dirname(__file__))
        self.flutter_android_caps = os.path.join(
            self.cur_path, r"../desired_caps/flutter-android.json"
        )
        self.flutter_ios_caps = os.path.join(
            self.cur_path, r"../desired_caps/flutter-ios.json"
        )
        self.native_android_caps = os.path.join(
            self.cur_path, r"../desired_caps/native-android.json"
        )
        self.native_ios_caps = os.path.join(
            self.cur_path, r"../desired_caps/native-ios.json"
        )

    @staticmethod
    def load_json_data(json_file):
        """
        This methods is used for loading json file data
        :return: it returns json records
        """
        records = None
        try:
            with open(json_file, "r") as read_file:
                records = json.load(read_file)
        except Exception as ex:
            traceback.print_exc(ex)

        return records

    def get_desired_caps(self, platform):
        desired_caps = {
            "flutter_android": self.load_json_data(self.flutter_android_caps),
            "flutter_ios": self.load_json_data(self.flutter_ios_caps),
            "native_android": self.load_json_data(self.native_android_caps),
            "native_ios": self.load_json_data(self.native_ios_caps),
        }
        return desired_caps.get(
            platform, self.load_json_data(self.flutter_android_caps)
        )
