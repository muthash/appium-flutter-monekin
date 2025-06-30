from finders.flutter_finders import FlutterFinder


class DashboardPageObjects:
    def __init__(self, driver):
        self.driver = driver
        self.flutter = FlutterFinder(driver)

    def get_dashboard_title(self):
        return self.flutter.by_text("Welcome again!")

    def get_expense_tag(self):
        return self.flutter.by_text("Expense")

    def get_expense_amount(self):
        return self.flutter.by_text("$0")

    def get_income_tag(self):
        return self.flutter.by_text("Income")

    def get_create_account_button(self):
        return self.flutter.by_text("Create Account")
