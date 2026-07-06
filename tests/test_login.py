from helper_functions.logging import log_info
from tests.assertions.login_assertions import assert_login_result


def test_user_login(login_page,username,password,expected):
    """Verify login behavior for valid and invalid credentials."""

    log_info(f"Testing login with user '{username}', "
             f"expected result '{expected}'")

    login_page.enter_login_credentials(username,password,)

    login_page.tap_login_btn()

    assert_login_result(login_page,username,expected,)
