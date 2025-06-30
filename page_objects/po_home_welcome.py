from finders.flutter_finders import FlutterFinderWrapper


class HomePageObjects:
    def __init__(self, driver):
        self._driver = driver
        self._finder = FlutterFinderWrapper(self._driver)

    def get_logo_icon(self):
        return self._finder.by_type("Image")

    def get_welcome_title(self):
        return self._finder.by_text("Monekin")

    def get_welcome_subtitle(self):
        return self._finder.by_text("Your personal finance manager")

    def get_welcome_subtitle2(self):
        return self._finder.by_text(f"100% open, 100% free")

    def get_offline_descr_title(self):
        return self._finder.by_text("OFFLINE ACCOUNT:")

    def get_offline_descr(self):
        return self._finder.by_text(
            "Your data will only be stored on your device, and will be safe as long as you don't uninstall the app or change phone. "
            "To prevent data loss, it is recommended to make a backup regularly from the app settings."
        )

    def get_login_button(self):
        return self._finder.by_text("Start session offline")

    def welcome_footer(self):
        return self._finder.by_text(
            "By logging in you agree to the Privacy Policy and the Terms of Use of the application"
        )
