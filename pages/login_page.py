from playwright.sync_api import Page, expect
from .base_page import BasePage
from utils.logger import get_logger

logger = get_logger(__name__)

class LoginPage(BasePage):
    """Page Object for Login functionality."""
    def __init__(self, page: Page):
        self.page: Page = page
        super().__init__(self.page)
        logger.debug("Login initialized")

    def user_login(self, username,password)-> None:
        """Login User,"""
        logger.debug("Login User with given credentials.")
        self.enter_username(username=username)
        self.enter_password(password=password)
        self.tap_login_btn()

    def navigate_to_login_page(self) -> None:
        """Navigate to Login Page."""
        logger.info("Navigating to Login Page.")
        self.page.locator("#home-header").get_by_role("link", name="Test Cases").click()

        iframe_close_button = self.page.frame_locator('iframe[name="aswift_9"]').get_by_role("button", name="Close ad")
        if iframe_close_button.count() > 0:
            iframe_close_button.click()

        self.page.get_by_role("link", name="Login Test Cases").click()
        self.page.get_by_role("link", name="page").click()

    def tap_login_btn(self)-> None:
        """Press Login Button"""
        logger.info("Tap login button.")
        self.page.get_by_role("button", name="Login").click()

    def is_logged_in(self) -> bool:
        """Verify successful login."""
        return self.page.get_by_role("link", name="Logout").is_visible(timeout=0)

    def verify_logged_in(self) -> None:
        """Assert successful login."""
        expect(self.page.locator("b")).to_contain_text("You logged into a secure area!")

    def verify_invalid_user_name(self)-> None:
        """Assert Invalid User name entered."""
        expect(self.page.locator("#flash")).to_contain_text("Your username is invalid!")

    def verify_invalid_password(self) -> None:
        """Assert Invalid User name entered."""
        expect(self.page.locator("#flash")).to_contain_text("Your password is invalid!")

