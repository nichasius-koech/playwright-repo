import pytest
from data.login_test_data import LoginResult
from tests.assertions.login_assertions import assert_login_result
from utils.logger import get_logger

logger = get_logger(__name__)

@pytest.mark.parametrize(
    "username,password,expected",
    [pytest.param("Practice",
                  "SuperSecretPassword!",
                  LoginResult.SUCCESS,
                  id="Valid login"),
     pytest.param("InvalidName",
                  "SuperSecretPassword!",
                  LoginResult.WRONG_USER,
                  id="Wrong user"),
     pytest.param("Practice",
                  "WrongPassword",
                  LoginResult.WRONG_PASSWORD,
                  id="Wrong password")
     ])
def test_user_login(login_page, username, password, expected):
    """Verify login behavior for valid and invalid credentials."""
    logger.debug(f"Verify login behavior for : "
                 f"\n Username: {username},"
                 f"\n Password: {password},"
                 f"\n Expected: {expected}.")
    login_page.enter_login_credentials(username, password)
    login_page.tap_login_btn()
    assert_login_result(login_page, username, expected)

