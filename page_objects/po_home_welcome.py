from finders.flutter_finders import FlutterFinder


class HomePageObjects:
    def __init__(self, driver):
        self.driver = driver
        self.flutter = FlutterFinder(driver)

    def get_logo_icon(self):
        return self.flutter.by_type("Image")

    def get_welcome_title(self):
        return self.flutter.by_text("Monekin")

    def get_welcome_subtitle(self):
        return self.flutter.by_text("Your personal finance manager")

    def get_welcome_subtitle2(self):
        return self.flutter.by_text(f"100% open, 100% free")

    def get_offline_descr_title(self):
        return "OFFLINE ACCOUNT:"

    def get_offline_descr(self):
        return (
            "Your data will only be stored on your device, and will be safe as long as you don't uninstall the app or change phone. "
            "To prevent data loss, it is recommended to make a backup regularly from the app settings."
        )

    def get_login_button(self):
        return self.flutter.by_text("loginButton")

    def welcome_footer(self):
        return "By logging in you agree to the Privacy Policy and the Terms of Use of the application"
