from finders.flutter_finders import FlutterFinderWrapper


class HomeSelectCountryPageObjects:
    def __init__(self, driver):
        self._driver = driver
        self._finder = FlutterFinderWrapper(self._driver)

    def get_sl1_title(self):
        return self._finder.by_text("Select your currency")

    def get_sl1_descr(self):
        return self._finder.by_text(
            "Your default currency will be used in reports and general charts. You will be able to change the currency and the app language later at any time in the application settings"
        )

    def get_select_currency_dropdown(self, currency="US Dollar"):
        return self._finder.by_text(currency)

    def get_select_currency_dropdown_search(self):
        return self._finder.by_semantics_label("Tap to search")

    def get_select_currency_dropdown_item(self, currency_name="Kenyan Shilling"):
        return self._finder.by_text(currency_name)

    def get_select_currency_dropdown_save(self):
        return self._finder.by_text("Save")

    def get_next_button(self):
        return self._finder.by_text("Next")
