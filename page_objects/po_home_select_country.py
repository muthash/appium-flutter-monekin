from finders.flutter_finders import FlutterFinder


class HomeSelectCountryPageObjects:
    def __init__(self, driver):
        self.driver = driver
        self.flutter = FlutterFinder(driver)

    def get_sl1_title(self):
        return self.flutter.by_text("Select your currency")

    def get_sl1_descr(self):
        return self.flutter.by_text(
            "Your default currency will be used in reports and general charts. You will be able to change the currency and the app language later at any time in the application settings"
        )

    def get_select_currency_dropdown(self):
        return self.flutter.by_text("Select your currency")

    def get_select_currency_dropdown_search(self):
        return self.flutter.by_type("TextField", index=0)

    def get_select_currency_dropdown_item(self, currency_name="Kenya Shilling"):
        return self.flutter.by_text(currency_name)

    def get_select_currency_dropdown_save(self):
        return self.flutter.by_text("Save")

    def get_next_button(self):
        return self.flutter.by_text("Next")
