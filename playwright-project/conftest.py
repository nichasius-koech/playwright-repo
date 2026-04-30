import pytest
from playwright.sync_api import Page
from pages import LoginPage

@pytest.fixture
def login(page: Page):
    login_page = LoginPage(page)
    login_page.load_page("https://practice.expandtesting.com/login")
    yield login_page
    page.close()


