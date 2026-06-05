import re
from typing import List
from playwright.sync_api import Page
from .base_page import BasePage
from utils.logger import get_logger

logger = get_logger(__name__)

class DynamicTable(BasePage):
    """Page Object for dynamic table functionalities."""
    def __init__(self, page: Page):
        self.page: Page = page
        super().__init__(self.page)

    @property
    def table(self):
        """Return table locator."""
        return self.page.locator("table.table.table-striped")

    def get_table_headers(self) -> List[str]:
        """Return table headers."""
        logger.info("Fetching Table Headers.")
        headers = self.page.locator("table.table.table-striped thead tr th")
        return headers.all_text_contents()

    def get_table_rows(self)-> list[str] :
        """Get all Table rows."""
        logger.info("Get all Table Rows.")
        table_rows = self. page.locator("table.table.table-striped tbody tr")
        return table_rows.all_text_contents()

    def get_actual_chrome_cpu_val(self) -> float:
        """Get Actual Chrome value from the Label."""
        logger.info("Get Actual CPU Value from Label.")
        cpu_text = self.page.locator("#chrome-cpu").text_content()
        return float(re.search(r"\d+(?:\.\d+)?", cpu_text).group())

    def get_table_chrome_cpu_val(self) -> float:
        """Get Chrome value in the Dynamic Table Where row header is 'Chrome' and Table header is 'CPU'."""
        logger.info("Get Actual CPU Value from Table cell.")
        cpu_index = self.get_table_headers().index("CPU")
        row = self.page.locator("tbody tr", has_text="Chrome")
        cpu_value = row.locator("td").nth(cpu_index).text_content()
        return float(re.search(r"\d+(?:\.\d+)?", cpu_value).group())



