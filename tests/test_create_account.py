from finders.flutter_finders import FlutterFinderActions
from page_objects.po_home_welcome import HomePageObjects
from page_objects.po_home_select_country import HomeSelectCountryPageObjects
from page_objects.po_home_data_policy import HomeDataPolicyPageObjects
from page_objects.po_home_contact_notice import HomeContactNoticePageObjects
from page_objects.po_dashboard import DashboardPageObjects
from page_objects.po_create_account import CreateAccountPageObjects


def test_create_account(driver):
    flutter_page_actions = FlutterFinderActions(driver)
    home_pom = HomePageObjects(driver)
    home_select_country_pom = HomeSelectCountryPageObjects(driver)
    home_data_policy_pom = HomeDataPolicyPageObjects(driver)
    home_contact_notice_pom = HomeContactNoticePageObjects(driver)
    dashboard_pom = DashboardPageObjects(driver)
    create_account_pom = CreateAccountPageObjects(driver)

    # Navigate to dashboard
    flutter_page_actions.assert_text(home_pom.get_welcome_title(), "Monekin")
    flutter_page_actions.tap(home_pom.get_login_button())
    flutter_page_actions.assert_text(
        home_select_country_pom.get_sl1_title(), "Select your currency"
    )
    flutter_page_actions.tap(home_select_country_pom.get_next_button())
    flutter_page_actions.assert_text(
        home_data_policy_pom.get_sl2_title(), "Safe, private and reliable"
    )
    flutter_page_actions.tap(home_data_policy_pom.get_next_button())
    flutter_page_actions.assert_text(
        home_contact_notice_pom.get_last_slide_title(), "All ready"
    )
    flutter_page_actions.tap(home_contact_notice_pom.get_continue_button())
    flutter_page_actions.assert_text(
        dashboard_pom.get_dashboard_title(), "Welcome again!"
    )

    # Navigate to create account page
    flutter_page_actions.tap(dashboard_pom.get_create_account_button())

    # create account
    flutter_page_actions.assert_text(
        create_account_pom.get_create_account_title(), "Create Account"
    )
    flutter_page_actions.enter_text(create_account_pom.get_account_name_input, " Rent")
    flutter_page_actions.enter_text(
        create_account_pom.get_initial_balance_input, "1000"
    )
    flutter_page_actions.tap(create_account_pom.get_currency_dropdown())
    flutter_page_actions.enter_text(
        create_account_pom.get_select_currency_dropdown_search(), "Kenya Shilling"
    )
    flutter_page_actions.tap(
        create_account_pom.get_select_currency_dropdown_item("Kenya Shilling")
    )
    flutter_page_actions.tap(create_account_pom.get_select_currency_dropdown_save())
    flutter_page_actions.tap(create_account_pom.get_currency_type())
    flutter_page_actions.tap(create_account_pom.get_create_account_button())

    flutter_page_actions.assert_text(
        dashboard_pom.get_dashboard_title(), "Welcome again!"
    )
