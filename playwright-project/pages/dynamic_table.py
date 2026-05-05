import re
from typing import List
from playwright.sync_api import Page, expect
from .base_page import BasePage

class DynamicTable(BasePage):
    """Page Object for dynamic table functionalities."""
    def __init__(self, page: Page):
        self.page: Page = page
        super().__init__(self.page)
        self.table = page.locator("table.table.table-striped")

    def get_table_headers(self) -> List[str]:
        """Return table headers."""
        headers = self.page.locator("table.table.table-striped thead tr th")
        table_headers: List[str] = headers.all_text_contents()
        return table_headers

    def get_table_rows(self)-> list[str] :
        """Get all Table rows."""
        table_rows = self. page.locator("table.table.table-striped tbody tr").all_text_contents()
        return table_rows

    def get_actual_chrome_cpu_val(self) -> float:
        """Get Actual Chrome value from the Label."""
        cpu_text = self.page.locator("#chrome-cpu").text_content()
        return float(re.search(r"\d+(?:\.\d+)?", cpu_text).group())

    def get_table_chrome_cpu_val(self) -> float:
        """Get Chrome value in the Dynamic Table Where row header is 'Chrome' and Table header is 'CPU'."""
        cpu_index = self.get_table_headers().index("CPU")
        row = self.page.locator("tbody tr", has_text="Chrome")
        cpu_value = row.locator("td").nth(cpu_index).text_content()
        return float(re.search(r"\d+(?:\.\d+)?", cpu_value.strip()).group())



