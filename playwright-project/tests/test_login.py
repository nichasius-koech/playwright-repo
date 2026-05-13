import pytest


class TestLogin:
    """Login TestSuite."""

    @pytest.mark.parametrize(
        "username,password,expected",
        [pytest.param("Practice", "SuperSecretPassword!", "Success",
                         id="Valid Registration Details"),
         pytest.param("InvalidName", "SuperSecretPassword!", "wrong_user",
                         id="Wrong User"),
         pytest.param("Practice", "WrongPassword", "wrong_password",
                         id="Wrong Password")])
    def test_user_registration(self, login_page,username, password,expected):
        """Test User Registration."""
        login_page.user_login(username, password)

        if expected == "success":
            login_page.verify_logged_in()
            assert login_page.is_logged_in(), "User login Failed !"

        elif expected == "wrong_user":
            login_page.verify_invalid_user_name()
            assert not login_page.is_logged_in(), "User logged in with invalid user !"

        elif expected == "wrong_password":
            login_page.verify_invalid_password()
            assert not login_page.is_logged_in(), "User logged in with invalid password !"

