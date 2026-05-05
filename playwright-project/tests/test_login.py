class TestLogin:
    """Login TestSuite."""
    def test_correct_credentials_login(self, login):
        """Test Loging in with correct credentials."""
        login.enter_user_name("practice")
        login.enter_password("SuperSecretPassword!")
        login.tap_login_btn()
        login.verify_logged_in()
        assert  login.is_logged_in(), "User login Failed !"

    def test_invalid_user_name(self, login):
        """Test Loging in with invalid username."""
        login.enter_user_name("InvalidName")
        login.enter_password("SuperSecretPassword!")
        login.tap_login_btn()
        login.verify_invalid_user_name()
        assert not login.is_logged_in(), "User logged in with invalid user !"

    def test_invalid_password_login(self, login):
        """Test Loging in with invalid password."""
        login.enter_user_name("practice")
        login.enter_password("WrongPassword")
        login.tap_login_btn()
        login.verify_invalid_password()
        assert not login.is_logged_in(), "User logged in with invalid password !"