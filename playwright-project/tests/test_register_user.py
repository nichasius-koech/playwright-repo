class TestUserRegistration:
    """Login TestSuite."""
    def test_valid_credentials(self, register, user_name):
        """Test Registration with valid credentials."""
        register.enter_user_name(user_name)
        register.enter_password("Dest1nation+")
        register.confirm_password("Dest1nation+")
        register.tap_register_btn()
        register.registration_success()
        assert register.is_login_page(), "Registration Failed !!"

    def test_invalid_password(self, register):
        """Test Registration with invalid password.
        Only Alphabetical letters without numbers or special characters."""
        register.enter_user_name("Practice4")
        register.enter_password("SuperSecretPassword")
        register.confirm_password("SuperSecretPassword")
        register.tap_register_btn()
        register.failed_registration()
        assert register.is_register_page(), "Registration Succeeded !!"


    def test_password_mismatch(self, register, user_name):
        """Test Registration with confirmation password mismatch."""
        register.enter_user_name(user_name)
        register.enter_password("Dest1nation+")
        register.confirm_password("Dest1nation!")
        register.tap_register_btn()
        register.password_mismatch()
        assert register.is_register_page(), "Registration Succeeded !!"
