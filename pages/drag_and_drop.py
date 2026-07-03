from logging import exception

from playwright.sync_api import Page, expect, Locator
from .base_page import BasePage
from utils.logger import get_logger

logger = get_logger(__name__)

class DragDropPage(BasePage):
    """Page Object for Drag and Drop functionality."""
    def __init__(self, page: Page):
        self.page: Page = page
        super().__init__(self.page)
        self.source = page.locator("#column-a")
        self.target = page.locator("#column-b")

    @staticmethod
    def is_element_visible(elem: Locator)-> bool:
        """Verify element is visible."""
        return elem.is_visible()

    def drag_and_drop(self,element_a: Locator , element_b: Locator)-> None:
        """Drag element a to element b"""
        logger.debug(f"Drag {element_a} to {element_b}")

        element_a.wait_for(state="visible")
        element_b.wait_for(state="visible")

        overlay = self.page.locator(".fc-dialog-overlay")

        try:
            if overlay.is_visible():
                overlay.wait_for(state="hidden")
            element_a.drag_to(element_b)
        except:
               raise TimeoutError
