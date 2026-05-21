from playwright.sync_api import Page

class BasePage:
    """Base Page functionalities."""

    def __init__(self, page: Page):
        self.page = page

    def load_page(self, url: str) -> None:
        """Navigate to URL."""
        self.page.goto(url, timeout=20_000)
        self.page.wait_for_load_state("domcontentloaded")

    def save_screenshot(self, screenshot_path, screenshot_name):
        """Save screenshot."""
        self.page.screenshot(path=f"{screenshot_path}/{screenshot_name}.png")

    def enter_user_name(self, user_name:str) -> None:
        """Enter the User Login  Name."""
        self.page.get_by_role("textbox", name="Username").fill(user_name)

    def enter_password(self, password: str) -> None:
        password_field = self.page.get_by_role("textbox", name="Password", exact=True)
        password_field.fill(password)

    def is_login_page(self) -> bool:
        """Verify Login Page is opened."""
        return self.page.get_by_role("button", name="Login").is_visible(timeout=0)

    def is_register_page(self) -> bool:
        """Verify Registration Page is opened."""
        return self.page.get_by_role("button", name="Register").is_visible(timeout=0)