import os

BASE_URL = os.getenv("BASE_URL", "https://practice.expandtesting.com")
LOGIN_URL = f"{BASE_URL}/login"
REGISTER_URL=f"{BASE_URL}/register"
DYN_TABLE_URL = f"{BASE_URL}/dynamic-table"
TEST_RESULTS = "./test-results/"