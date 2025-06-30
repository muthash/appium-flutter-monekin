from finders.flutter_finders import FlutterFinderActions
from page_objects.po_home_welcome import HomePageObjects
from page_objects.po_home_select_country import HomeSelectCountryPageObjects
from page_objects.po_home_data_policy import HomeDataPolicyPageObjects
from page_objects.po_home_contact_notice import HomeContactNoticePageObjects
from page_objects.po_dashboard import DashboardPageObjects


def test_navigate_to_home_screen(driver):
    flutter_page_actions = FlutterFinderActions(driver)
    home_pom = HomePageObjects(driver)
    home_select_country_pom = HomeSelectCountryPageObjects(driver)
    home_data_policy_pom = HomeDataPolicyPageObjects(driver)
    home_contact_notice_pom = HomeContactNoticePageObjects(driver)
    dashboard = DashboardPageObjects(driver)

    # Verify the app is launched and the home page is displayed
    flutter_page_actions.assert_element_present("logo", "id", 10)
    flutter_page_actions.assert_element_present("loginButton", "text", 10)
    flutter_page_actions.assert_text(home_pom.get_welcome_title(), "Monekin")
    flutter_page_actions.assert_text(
        home_pom.get_welcome_subtitle(), "Your personal finance manager"
    )
    flutter_page_actions.assert_text(
        home_pom.get_welcome_subtitle2(), f"100% open, 100% free"
    )
    flutter_page_actions.assert_text(
        home_pom.get_offline_descr_title(), "OFFLINE ACCOUNT:"
    )
    flutter_page_actions.assert_text(
        home_pom.get_offline_descr(),
        "Your data will only be stored on your device, and will be safe as long as you don't uninstall the app or change phone. "
        "To prevent data loss, it is recommended to make a backup regularly from the app settings.",
    )
    flutter_page_actions.assert_text(
        home_pom.welcome_footer(),
        "By logging in you agree to the Privacy Policy and the Terms of Use of the application",
    )
    flutter_page_actions.tap(home_pom.get_login_button())

    # Verify select country and currency screen
    flutter_page_actions.assert_element_present("Select your currency", "text", 10)
    flutter_page_actions.assert_text(
        home_select_country_pom.get_sl1_title(), "Select your currency"
    )
    flutter_page_actions.assert_text(
        home_select_country_pom.get_sl1_descr(),
        "Your default currency will be used in reports and general charts. You will be able to change the currency and the app language later at any time in the application settings",
    )
    flutter_page_actions.tap(home_select_country_pom.get_select_currency_dropdown())
    flutter_page_actions.enter_text(
        home_select_country_pom.get_select_currency_dropdown_search(), "Kenya Shilling"
    )
    flutter_page_actions.tap(
        home_select_country_pom.get_select_currency_dropdown_item("Kenya Shilling")
    )
    flutter_page_actions.tap(
        home_select_country_pom.get_select_currency_dropdown_save()
    )
    flutter_page_actions.tap(home_select_country_pom.get_next_button())

    # Verify data policy screen
    flutter_page_actions.assert_element_present(
        "Safe, private and reliable", "text", 10
    )
    flutter_page_actions.assert_text(
        home_data_policy_pom.get_sl2_title(), "Safe, private and reliable"
    )
    flutter_page_actions.assert_text(
        home_data_policy_pom.get_sl2_descr(),
        "Your data is only yours. We store the information directly on your device, without going through external servers. This makes it possible to use the app even without internet",
    )
    flutter_page_actions.assert_text(
        home_data_policy_pom.get_sl2_descr2(),
        "Also, the source code of the application is public, anyone can collaborate on it and see how it works",
    )
    flutter_page_actions.tap(home_data_policy_pom.get_next_button())

    # Verify contact notice screen
    flutter_page_actions.assert_element_present("All ready", "text", 10)

    flutter_page_actions.assert_text(
        home_contact_notice_pom.get_last_slide_title(), "All ready"
    )
    flutter_page_actions.assert_text(
        home_contact_notice_pom.get_last_slide_descr(),
        "With Monekin, you can finally achieve the financial independence you want so much. You will have graphs, budgets, tips, statistics and much more about your money.",
    )
    flutter_page_actions.assert_text(
        home_contact_notice_pom.get_last_slide_descr2(),
        "We hope you enjoy your experience! Do not hesitate to contact us in case of doubts, suggestions...",
    )
    flutter_page_actions.tap(home_contact_notice_pom.get_continue_button())

    # Assert Dashboard is displayed
    flutter_page_actions.assert_element_present("Welcome again!", "text", 10)
    flutter_page_actions.assert_text(dashboard.get_dashboard_title(), "Welcome again!")
    flutter_page_actions.assert_text(dashboard.get_expense_tag(), "Expense")
