from finders.flutter_finders import FlutterFinderWrapper


class HomeContactNoticePageObjects:
    def __init__(self, driver):
        self._driver = driver
        self._finder = FlutterFinderWrapper(self._driver)

    def get_last_slide_title(self):
        return self._finder.by_text("All ready")

    def get_last_slide_descr(self):
        return self._finder.by_text(
            "With Monekin, you can finally achieve the financial independence you want so much. You will have graphs, budgets, tips, statistics and much more about your money."
        )

    def get_last_slide_descr2(self):
        return self._finder.by_text(
            "We hope you enjoy your experience! Do not hesitate to contact us in case of doubts, suggestions..."
        )

    def get_continue_button(self):
        return self._finder.by_text("Continue")
