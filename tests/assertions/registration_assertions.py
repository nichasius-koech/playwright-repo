from data.registration_test_data import RegisterResult

def assert_registration_success(register_page, username)-> None:
    """Verify registration login with valid credentials."""
    register_page.registration_success()
    assert (register_page.is_login_page()
            ), f"User should be redirected to login: {username}"


def assert_missing_fields(register_page, username)-> None:
    """Verify registration with missing fields."""
    register_page.missing_field()
    assert (register_page.is_register_page()
            ), f"Registration should fail due to missing fields: {username}"


def assert_password_mismatch(register_page, username)-> None:
    """Verify login with wrong password."""
    register_page.password_mismatch()
    assert (register_page.is_register_page()
            ), f"Registration should fail due to password mismatch: {username}"


REGISTRATION_VALIDATORS = {
    RegisterResult.SUCCESS: assert_registration_success,
    RegisterResult.MISSING_FIELD: assert_missing_fields,
    RegisterResult.PASSWORD_MISSMATCH: assert_password_mismatch}

def assert_registration_result(register_page, username, expected)-> None:
    """Verify registration input against expected output"""
    validator = REGISTRATION_VALIDATORS.get(expected)

    if validator is None:
        raise ValueError(
            f"Unsupported registration result: {expected}")
    validator(register_page, username)
