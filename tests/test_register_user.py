import pytest

from data.registration_test_data import RegisterResult
from helper_functions.logging import log_debug
from tests.assertions.registration_assertions import assert_registration_result


@pytest.mark.parametrize(
    "password,confirm_password,expected",
    [pytest.param( "Dest1nation+",
                   "Dest1nation+",
                   RegisterResult.SUCCESS,
                   id="Valid registration"),
     pytest.param( "",
                   "SuperSecretPassword",
                   RegisterResult.MISSING_FIELD,
                   id="Missing password"),
     pytest.param( "SuperSecretPasswoh+",
                   "SuperSecretPasswor!",
                   RegisterResult.PASSWORD_MISSMATCH,
                   id="Password mismatch")
     ])
def test_user_registration(register_page, username, password, confirm_password, expected):
    """Verify registration behavior with valid and invalid inputs."""
    log_debug(f"Verify registration behavior for : "
                 f"\n Username: {username},"
                 f"\n Password: {password},"
                 f"\n Expected: {expected}.")
    register_page.register_user(username, password, confirm_password)
    assert_registration_result(register_page, username, expected)