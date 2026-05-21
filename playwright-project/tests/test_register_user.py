import pytest


@pytest.mark.parametrize(
    "password,confirm_password,expected",
    [pytest.param( "Dest1nation+", "Dest1nation+", "success",
                      id="Valid registration"),
     pytest.param( "", "SuperSecretPassword", "missing_field",
                      id="Missing password"),
     pytest.param( "SuperSecretPasswoh+", "SuperSecretPasswor!", "mismatch",
                      id="Password mismatch")])
def test_user_registration(register_page, user_name, password, confirm_password, expected):
    """Verify registration behavior with valid and invalid inputs."""

    register_page.register_user(user_name, password, confirm_password)
    assert_registration_result(register_page, user_name, expected)


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