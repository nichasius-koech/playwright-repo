from data.login_test_data import LoginResult


def assert_login_success(login_page, username)-> None:
    """Verify successful login with correct credentials."""
    login_page.verify_logged_in()
    assert login_page.is_logged_in(), (
        f"User should be logged in: {username}")


def assert_wrong_username(login_page, username)-> None:
    """Verify login with invalid username."""
    login_page.verify_invalid_user_name()
    assert not login_page.is_logged_in(), (
        f"Login succeeded unexpectedly for invalid user: {username}")


def assert_wrong_password(login_page, username)-> None:
    """Verify login with wrong password."""
    login_page.verify_invalid_password()
    assert not login_page.is_logged_in(), (
        f"Login succeeded unexpectedly with wrong password for: {username}")


LOGIN_VALIDATORS = {
    LoginResult.SUCCESS: assert_login_success,
    LoginResult.WRONG_USER: assert_wrong_username,
    LoginResult.WRONG_PASSWORD: assert_wrong_password}

def assert_login_result(login_page, username, expected)-> None:
    """Verify input against expected output"""
    validator = LOGIN_VALIDATORS.get(expected)

    if validator is None:
        raise ValueError(
            f"Unsupported login result: {expected}")
    validator(login_page, username)
