import os
import random
import pytest
import base64
import yaml
from pathlib import Path
from pytest_html import extras
from playwright.sync_api import Page

from helper_functions.logging import log_info, log_error
from pages.drag_and_drop import DragDropPage
from pages.login_page import LoginPage
from pages.dynamic_table import DynamicTable
from pages.register_page import RegisterPage
from utils.config import LOGIN_URL, DYN_TABLE_URL, REGISTER_URL, DRAG_DROP_URL
from dotenv import load_dotenv

load_dotenv()


def load_yaml(filename: str) -> dict:
    """Load yaml test data."""
    file_path = Path(__file__).parent / "data" / filename

    with file_path.open(encoding="utf-8") as file:
        return yaml.safe_load(file)

def user_name():
    """Generate a random username."""
    log_info("Generating a Username.")
    from faker import Faker
    full_name = Faker()
    rand_num = random.randint(1, 10)
    return f"{full_name.first_name()}{rand_num}"

def generate_regisration_tests(metafunc):

    if {"register_page", "username", "password","confirm_password",  "expected"} <= set(metafunc.fixturenames):

        data = load_yaml("registration_tests.yaml")

        test_cases = []
        ids = []

        for case in data["registration_tests"]:
            password = os.getenv(case["password_env"])
            confirm_password = os.getenv(case["confirm_password"])
            username = user_name()

            test_cases.append(
                (username,
                 password,
                 confirm_password,
                 case["expected"],))

            ids.append(case["id"])

        metafunc.parametrize(("username", "password", "confirm_password",  "expected"), test_cases,ids=ids,)

def generate_login_tests(metafunc):
    if {"login_page", "username", "password", "expected"} <= set(metafunc.fixturenames):

        data = load_yaml("login_tests.yaml")

        test_cases = []
        ids = []

        for case in data["login_tests"]:
            password = os.getenv(case["password_env"])

            test_cases.append(
                (case["username"],
                 password,
                 case["expected"],))

            ids.append(case["id"])

        metafunc.parametrize(("username", "password", "expected"), test_cases,ids=ids,)

def pytest_generate_tests(metafunc):
    """Central test generator hook."""
    generate_login_tests(metafunc)
    generate_regisration_tests(metafunc)

def pytest_bdd_before_scenario(feature, scenario):
    """Log the feature and scenario names before scenario execution."""
    log_info("=" * 80)
    log_info(f"Feature : {feature.name}")
    log_info(f"Scenario: {scenario.name}")
    log_info("=" * 80)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:

        page = item.funcargs.get("page")

        if page:
            screenshot_path = Path("screenshots")
            screenshot_path.mkdir(exist_ok=True)
            file_name = screenshot_path / f"{item.name}.png"
            screenshot_bytes = page.screenshot(path=str(file_name))
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
            log_error(f"Screenshot saved: {file_name}")


@pytest.fixture
def login_page(request, page: Page):
    """Navigate to Login page Url."""
    log_info("Navigating to Login page")
    login_page = LoginPage(page)
    login_page.load_page(LOGIN_URL)
    yield login_page

@pytest.fixture
def dyn_table(page: Page):
    """Navigate to Url containing a dynamic table."""
    log_info("Navigating to Dynamic Table page")
    dynamic_table = DynamicTable(page)
    dynamic_table.load_page(DYN_TABLE_URL)
    yield dynamic_table

@pytest.fixture
def drag_drop(page: Page):
    """Navigate to Url containing a drag and drop elements."""
    log_info("Navigating to Drag & Drop page")
    # page.reload()
    drap_drop_page = DragDropPage(page)
    page.reload()
    drap_drop_page.load_page(DRAG_DROP_URL)
    yield drap_drop_page

@pytest.fixture
def register_page(page: Page):
    """Navigate to Register page Url."""
    log_info("Navigating to Registration page")
    register_page = RegisterPage(page)
    register_page.load_page(REGISTER_URL)
    yield register_page

# @pytest.fixture
# def username():
#     """Generate a random username."""
#     log_info("Generating a Username.")
#     from faker import Faker
#     full_name = Faker()
#     rand_num=random.randint(1,10)
#     yield f"{full_name.first_name()}{rand_num}"
