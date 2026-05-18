import pytest


@pytest.mark.parametrize(
    "username,password,expected",
    [
        pytest.param("Practice", "SuperSecretPassword!", "success", id="Valid login"),
        pytest.param("InvalidName", "SuperSecretPassword!", "wrong_user", id="Wrong user"),
        pytest.param("Practice", "WrongPassword", "wrong_password", id="Wrong password"),
    ],
)
def test_user_login(login_page, username, password, expected):
    """Verify login behavior for valid and invalid credentials."""
    
    login_page.user_login(username, password)
    assert_login_result(login_page, username, expected)


def assert_login_result(login_page, username, expected):
    if expected == "success":
        login_page.verify_logged_in()
        assert (login_page.is_logged_in()
                ), f"User should be logged in: {username}"

    elif expected == "wrong_user":
        login_page.verify_invalid_user_name()
        assert not (login_page.is_logged_in()
                    ), f"Login succeeded unexpectedly for invalid user: {username}"

    elif expected == "wrong_password":
        login_page.verify_invalid_password()
        assert not (login_page.is_logged_in()
                    ), f"Login succeeded unexpectedly with wrong password for: {username}"