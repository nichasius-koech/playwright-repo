from playwright.sync_api import Page, expect
from .base_page import BasePage
from utils.logger import get_logger

logger = get_logger(__name__)

class RegisterPage(BasePage):
    """Page Object for Login functionality."""
    def __init__(self, page: Page):
        self.page: Page = page
        super().__init__(self.page)
        logger.debug("Registration initialized")

    def confirm_password(self, password:str)-> None:
        """Confirm Password."""
        logger.info("Confirm User Password.")
        self.page.get_by_role("textbox", name="Confirm Password", exact=True).fill(password)

    def tap_register_btn(self)-> None:
        """Press Register Button"""
        logger.info("Tap Register Button.")
        self.page.get_by_role("button", name="Register").click()

    def register_user(self, username, password, password_confirm)-> None:
        """Register new User."""
        logger.debug("Register New User.")
        self.enter_username(username=username)
        self.enter_password(password=password)
        self.confirm_password(password=password_confirm)
        self.tap_register_btn()

    def registration_success(self)-> None:
        """Verify Register Success."""
        logger.debug("Confirm User Registration Successful.")
        expect(self.page.locator("#flash")).to_contain_text("Successfully registered")

    def failed_registration(self)-> None:
        """Verify Invalid Registration."""
        logger.info("Confirm User Registration Failed.")
        expect(self.page.locator("#flash")).to_contain_text("An error occurred during registration")

    def missing_field(self)-> None:
        """Verify Registration with missing field."""
        logger.info("Verify Missing Field alert.")
        expect(self.page.locator("#flash")).to_contain_text("All fields are required")

    def password_mismatch(self)-> None:
        """Verify Password Mismatch."""
        logger.info("Verify Password mismatch.")
        expect(self.page.locator("#flash")).to_contain_text("Passwords do not match")

