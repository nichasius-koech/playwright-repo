import pytest

class TestUserRegistration:
    """User Registration TestSuite."""

    @pytest.mark.parametrize(
        "password,confirm_password,expected",
        [pytest.param("Dest1nation+", "Dest1nation+", "success",
                         id="Valid Registration Details"),
         pytest.param("", "SuperSecretPassword", "missing_field",
                         id="Missing password field"),
         pytest.param("SuperSecretPasswoh+", "SuperSecretPasswor!", "mismatch",
                         id="Password Mismatch")])
    def test_user_registration(self, register_page, user_name, password, confirm_password, expected):
        """Test User Registration."""
        register_page.register_user(user_name, password, confirm_password)

        if expected == "success":
            register_page.registration_success()
            assert register_page.is_login_page(), "Registration Failed !!"

        elif expected == "missing_field":
            register_page.missing_field()
            assert register_page.is_register_page(), "Registration Succeeded !!"

        elif expected == "mismatch":
            register_page.password_mismatch()
            assert register_page.is_register_page(), "Registration Succeeded !!"
