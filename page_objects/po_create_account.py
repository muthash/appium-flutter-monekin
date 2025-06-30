from finders.flutter_finders import FlutterFinder


class CreateAccountPageObjects:
    def __init__(self, driver):
        self.driver = driver
        self.flutter = FlutterFinder(driver)

    def get_create_account_title(self):
        return self.flutter.by_text("Create Account")

    def get_icon_dropdown(self):
        return self.flutter.by_text("All ready")

    def get_color_dropdown(self):
        return self.flutter.by_text("Color")

    def get_account_name_input(self):
        return self.flutter.by_text("Account name *")

    def get_initial_balance_input(self):
        return self.flutter.by_text("Initial balamce *")

    def get_currency_dropdown(self):
        return self.flutter.by_text("Currency")

    def get_select_currency_dropdown_search(self):
        return self.flutter.by_type("TextField", index=0)

    def get_select_currency_dropdown_item(self, currency_name="Kenya Shilling"):
        return self.flutter.by_text(currency_name)

    def get_select_currency_dropdown_save(self):
        return self.flutter.by_text("Save")

    def get_currency_type(self):
        return self.flutter.by_text("Normal account")

    def get_create_account_button(self):
        return self.flutter.by_text("Create Account")
