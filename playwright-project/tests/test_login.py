class TestLogin:
    """Login TestSuite."""
    def test_correct_credentials_login(self, login):
        """Test Loging in with correct credentials."""
        login.enter_user_name("practice")
        login.enter_password("SuperSecretPassword!")
        login.tap_login_btn()
        login.assert_logged_in()
        assert  login.is_logged_in(), "User login Failed !"

    def test_invalid_user_name(self, login):
        """Test Loging in with invalid username."""
        login.enter_user_name("InvalidName")
        login.enter_password("SuperSecretPassword!")
        login.tap_login_btn()
        login.assert_invalid_password()
        assert not login.is_logged_in(), "User logged in with wrong password !"

    def test_invalid_password_login(self, login):
        """Test Loging in with invalid password."""
        login.enter_user_name("practice")
        login.enter_password("WrongPassword")
        login.tap_login_btn()
        login.assert_invalid_password()
        assert not login.is_logged_in(), "User logged in with wrong password !"