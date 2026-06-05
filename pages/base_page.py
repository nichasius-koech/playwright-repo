from pathlib import Path
from playwright.sync_api import Page
from utils.logger import get_logger

logger = get_logger(__name__)

class BasePage:
    """Base Page functionalities."""

    def __init__(self, page: Page):
        self.page = page
        logger.debug("BasePage initialized")

    @property
    def username_input(self):
        return self.page.get_by_role("textbox", name="Username")

    @property
    def password_field(self):
        return self.page.get_by_role("textbox", name="Password", exact=True)

    def load_page(self, url: str) -> None:
        """Navigate to URL."""
        logger.info(f"Navigating to URL: {url}")
        self.page.goto(url, timeout=20_000)
        logger.debug("Page navigation completed")

    def save_screenshot(self, screenshot_path: str, screenshot_name: str) -> None:
        """Save screenshot."""
        path = Path(screenshot_path) / f"{screenshot_name}.png"
        self.page.screenshot(path=str(path))
        logger.info(f"Screenshot saved at: {path}")

    def enter_username(self, username: str) -> None:
        """Fill username field."""
        logger.debug(f"Filling username: {username}")
        self.username_input.fill(username)

    def enter_password(self, password: str) -> None:
        """Fill password field."""
        logger.debug("Filling password field")
        self.password_field.fill(password)

    def is_login_page(self) -> bool:
        """Verify Login Page is opened."""
        visible = self.page.get_by_role("button", name="Login").is_visible()
        logger.debug(f"Login button visible: {visible}")
        return visible

    def is_register_page(self) -> bool:
        """Verify Registration Page is opened."""
        visible = self.page.get_by_role("button", name="Register").is_visible()
        logger.debug(f"Register button visible: {visible}")
        return visible