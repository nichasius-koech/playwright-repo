import random
import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.dynamic_table import DynamicTable
from pages.register_page import RegisterPage
from utils.config import LOGIN_URL, DYN_TABLE_URL, REGISTER_URL, TEST_RESULTS


import pytest
import base64
from pytest_html import extras

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:

        page = item.funcargs.get("page")

        if page:
            screenshot_bytes = page.screenshot()
            screenshot_b64 = base64.b64encode(screenshot_bytes).decode()

            #Custom HTML block
            html = f"""
            <div style="margin-top:20px; padding:10px; border:2px solid #f44336;">
                <h3 style="color:#f44336;"> {item.name} Failure Screenshot: </h3>
                <a href="data:image/png;base64,{screenshot_b64}" target="_blank">
                    <img src="data:image/png;base64,{screenshot_b64}" 
                         style="width:100%; max-width:1200px;" />
                </a>
            </div>
            """

            rep.extras = getattr(rep, "extras", [])
            rep.extras.append(extras.html(html))


@pytest.fixture
def login_page(request, page: Page):
    """Navigate to Login page Url."""
    login_page = LoginPage(page)
    login_page.load_page(LOGIN_URL)
    yield login_page

@pytest.fixture
def dyn_table(page: Page):
    """Navigate to Url containing a dynamic table."""
    dynamic_table = DynamicTable(page)
    dynamic_table.load_page(DYN_TABLE_URL)
    yield dynamic_table

@pytest.fixture
def register_page(page: Page):
    """Navigate to Register page Url."""
    register_page = RegisterPage(page)
    register_page.load_page(REGISTER_URL)
    yield register_page

@pytest.fixture
def user_name():
    """Generate a random username."""
    from faker import Faker
    full_name = Faker()
    rand_num=random.randint(1,10)
    yield f"{full_name.first_name()}{rand_num}"
