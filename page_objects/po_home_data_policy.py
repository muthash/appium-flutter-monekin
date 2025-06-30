from finders.flutter_finders import FlutterFinder


class HomeDataPolicyPageObjects:
    def __init__(self, driver):
        self.driver = driver
        self.flutter = FlutterFinder(driver)

    def get_sl2_title(self):
        return self.flutter.by_text("Safe, private and reliable")

    def get_sl2_descr(self):
        return self.flutter.by_text(
            "Your data is only yours. We store the information directly on your device, without going through external servers. This makes it possible to use the app even without internet"
        )

    def get_sl2_descr2(self):
        return self.flutter.by_text(
            "Also, the source code of the application is public, anyone can collaborate on it and see how it works"
        )

    def get_next_button(self):
        return self.flutter.by_text("Next")
