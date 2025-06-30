from appium_flutter_finder.flutter_finder import FlutterFinder
from finders.flutter_finders import FlutterFinderWrapper


class CreateAccountPageObjects:
    def __init__(self, driver):
        self._driver = driver
        self._flutter_finder = FlutterFinder()
        self._finder = FlutterFinderWrapper(self._driver)

    def get_create_account_title(self):
        return self._finder.by_text("Create account")

    def get_icon_dropdown(self):
        return self._finder.by_text("Icon")

    def get_color_dropdown(self):
        return self._finder.by_text("Color")

    def get_account_name_field(self):
        return self._finder.by_semantics_label("Account name *")

    def get_initial_balance_field(self):
        return self._finder.by_semantics_label("Initial balance *")

    def get_select_currency_dropdown(self, currency="US Dollar"):
        return self._finder.by_text(currency)

    def get_select_currency_dropdown_search(self):
        return self._finder.by_semantics_label("Tap to search")

    def get_select_currency_dropdown_item(self, currency_name="Kenyan Shilling"):
        return self._finder.by_text(currency_name)

    def get_select_currency_dropdown_save(self):
        return self._finder.by_text("Save")

    def get_account_type(self, account_type="Normal account"):
        return self._finder.by_text(account_type)

    def get_create_account_button(self):
        child = self._flutter_finder.by_text("Create account")
        ancestor = self._flutter_finder.by_type("_FilledButtonWithIcon")
        return self._finder.by_ancestor(child, ancestor)
