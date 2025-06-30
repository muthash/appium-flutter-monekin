from finders.flutter_finders import FlutterFinderWrapper


class DashboardPageObjects:
    def __init__(self, driver):
        self._driver = driver
        self._finder = FlutterFinderWrapper(self._driver)

    def get_dashboard_title(self):
        return self._finder.by_text("Welcome again!")

    def get_expense_tag(self):
        return self._finder.by_text("Expense")

    def get_expense_amount(self, amount="$0"):
        return self._finder.by_text(amount)

    def get_income_tag(self):
        return self._finder.by_text("Income")

    def get_income_amount(self, amount="$0"):
        return self._finder.by_text(amount)

    def get_create_account_button(self):
        return self._finder.by_text("Create Account")
