import random
import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.dynamic_table import DynamicTable
from pages.register_page import RegisterPage

BASE_URL = "https://practice.expandtesting.com"

@pytest.fixture
def login(page: Page):
    """Navigate to Login page Url."""
    login_page = LoginPage(page)
    login_page.load_page(f"{BASE_URL}/login")
    yield login_page
    page.close()

@pytest.fixture
def dyn_table(page: Page):
    """Navigate to Url containing a dynamic table."""
    dynamic_table = DynamicTable(page)
    dynamic_table.load_page(f"{BASE_URL}/dynamic-table")
    yield dynamic_table

@pytest.fixture
def register(page: Page):
    """Navigate to Register page Url."""
    register_page = RegisterPage(page)
    register_page.load_page(f"{BASE_URL}/register")
    yield register_page

@pytest.fixture
def user_name():
    """Generate a random username."""
    from faker import Faker
    full_name = Faker()
    rand_num=random.randint(1,10)
    yield f"{full_name.first_name()}{rand_num}"
