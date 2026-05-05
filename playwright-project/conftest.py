import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.dynamic_table import DynamicTable

@pytest.fixture
def login(page: Page):
    login_page = LoginPage(page)
    login_page.load_page("https://practice.expandtesting.com/login")
    yield login_page
    page.close()

@pytest.fixture
def dyn_table(page: Page):
    dynamic_table = DynamicTable(page)
    dynamic_table.load_page("https://practice.expandtesting.com/dynamic-table")
    yield dynamic_table
    page.close()

