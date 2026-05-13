from playwright.sync_api import Page, expect
from .base_page import BasePage

class RegisterPage(BasePage):
    """Page Object for Login functionality."""
    def __init__(self, page: Page):
        self.page: Page = page
        super().__init__(self.page)

    def confirm_password(self, password:str)-> None:
        """Confirm Password."""
        self.page.get_by_role("textbox", name="Confirm Password", exact=True).fill(password)

    def tap_register_btn(self)-> None:
        """Press Register Button"""
        self.page.get_by_role("button", name="Register").click()

    def register_user(self,user_name,password,password_confirm)-> None:
        """Register new User."""
        self.enter_user_name(user_name)
        self.enter_password(password)
        self.confirm_password(password_confirm)
        self.tap_register_btn()

    def registration_success(self)-> None:
        """Verify Register Success."""
        expect(self.page.locator("#flash")).to_contain_text("Successfully registered")

    def failed_registration(self)-> None:
        """Verify Invalid Registration."""
        expect(self.page.locator("#flash")).to_contain_text("An error occurred during registration")

    def missing_field(self)-> None:
        """Verify Registration with missing field."""
        expect(self.page.locator("#flash")).to_contain_text("All fields are required")

    def password_mismatch(self)-> None:
        """Verify Password Mismatch."""
        expect(self.page.locator("#flash")).to_contain_text("Passwords do not match")

