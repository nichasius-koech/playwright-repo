"""This module demonstrates pytest BDD example."""
from pathlib import Path
from pytest_bdd import scenarios, given, then, when
from conftest import logger
from helper_functions.logging import log_step, log_pass

feature_file_dir= "../features"
feature_file="login.feature"
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE=BASE_DIR.joinpath(feature_file_dir).joinpath().joinpath(feature_file)
scenarios(FEATURE_FILE)


@given("User navigates to Login Url")
def login_page_is_open(login_page):
    log_step(1, "Navigating to Login Page.")
    login_page.navigate_to_login_page()
    assert login_page.is_login_page(), "Login Page no open."

@given("Login widgets are displayed")
def login_widgets_are_displayed(login_page):
    log_step(2, "Verify Login Url is displayed.")
    login_page.is_login_url(), "Login page not loaded !"

@given("User enters correct user name and Password")
def enter_correct_credentials(login_page):
    log_step(3,"Enter correct user name and Password.")
    login_page.enter_login_credentials("practice", "SuperSecretPassword!")

@when("User clicks on Login button")
def click_login_button(login_page):
    """Click the Login button"""
    log_step(4,"Click the Login button.")
    login_page.tap_login_btn()

@then("User is successfully logged in")
def verify_user_logged_in(login_page):
    log_step(5,"Verify User is successfully logged in.")
    login_page.verify_logged_in()
    assert login_page.is_logged_in(), f"User should be logged in."

# Invalid Password Usecase
@given("User enters valid user name and wrong Password")
def enter_correct_credentials(login_page):
    logger.info("User enters valid user name and wrong Password.")
    login_page.enter_login_credentials("practice", "151212165!")

@when("User clicks on Login button")
def click_login_button(login_page):
    """Click the Login button"""
    logger.info("Click the Login button.")
    login_page.tap_login_btn()

@then("User is not logged in")
def verify_user_logged_in(login_page):
    logger.info("Verify User is successfully logged in.")
    login_page.verify_invalid_password()
    assert not login_page.is_logged_in(), f"User should be logged in."
