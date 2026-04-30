from playwright.sync_api import Page

class BasePage:
    """Base Page functionalities."""

    def __init__(self, page: Page):
        self.page = page

    def load_page(self, url: str) -> None:
        """Navigate to URL."""
        self.page.goto(url, timeout=10_000)
        self.page.wait_for_load_state("domcontentloaded")


