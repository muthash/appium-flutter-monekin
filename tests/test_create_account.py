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
    flutter_page_actions.assert_element_present(home_pom.get_logo_icon())
    flutter_page_actions.click_element(home_pom.get_login_button())

    flutter_page_actions.assert_element_present(home_select_country_pom.get_sl1_title())
    flutter_page_actions.click_element(home_select_country_pom.get_next_button())

    flutter_page_actions.assert_element_present(home_data_policy_pom.get_sl2_title())
    flutter_page_actions.click_element(home_data_policy_pom.get_next_button())

    flutter_page_actions.assert_element_present(
        home_contact_notice_pom.get_last_slide_title()
    )
    flutter_page_actions.click_element(home_contact_notice_pom.get_continue_button())

    flutter_page_actions.assert_element_present(dashboard_pom.get_dashboard_title())
    flutter_page_actions.assert_element_present(dashboard_pom.get_expense_tag())

    # Navigate to create account page
    flutter_page_actions.click_element(dashboard_pom.get_create_account_button())

    # create account
    flutter_page_actions.assert_element_present(
        create_account_pom.get_create_account_title()
    )
    flutter_page_actions.enter_text(
        create_account_pom.get_account_name_field(), "Samson Sam"
    )
    flutter_page_actions.enter_text(
        create_account_pom.get_initial_balance_field(), "1000"
    )
    flutter_page_actions.click_element(create_account_pom.get_account_type())
    flutter_page_actions.click_element(create_account_pom.get_create_account_button())

    flutter_page_actions.assert_element_present(dashboard_pom.get_dashboard_title())
    flutter_page_actions.assert_element_present(dashboard_pom.get_income_tag())
    flutter_page_actions.assert_element_present(
        dashboard_pom.get_total_balance_amount(amount="Ksh1000")
    )
