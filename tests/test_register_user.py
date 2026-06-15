import pytest
from utils.logger import get_logger

logger = get_logger(__name__)

@pytest.mark.parametrize(
    "password,confirm_password,expected",
    [pytest.param( "Dest1nation+", "Dest1nation+", "success",
                      id="Valid registration"),
     pytest.param( "", "SuperSecretPassword", "missing_field",
                      id="Missing password"),
     pytest.param( "SuperSecretPasswoh+", "SuperSecretPasswor!", "mismatch",
                      id="Password mismatch")])
def test_user_registration(register_page, username, password, confirm_password, expected):
    """Verify registration behavior with valid and invalid inputs."""
    logger.debug(f"Verify registration behavior for : "
                 f"\n Username: {username},"
                 f"\n Password: {password},"
                 f"\n Expected: {expected}.")
    register_page.register_user(username, password, confirm_password)
    assert_registration_result(register_page, username, expected)


def assert_registration_result(register_page, user_name, expected):
    if expected == "success":
        register_page.registration_success()
        assert (register_page.is_login_page()
                ), f"User should be redirected to login: {user_name}"
        return

    if expected == "missing_field":
        register_page.missing_field()
        assert (register_page.is_register_page()
                ), f"Registration should fail due to missing fields: {user_name}"
        return

    if expected == "mismatch":
        register_page.password_mismatch()
        assert (register_page.is_register_page()
                ), f"Registration should fail due to password mismatch: {user_name}"