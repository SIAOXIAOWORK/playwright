import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture()
def browser_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        yield page
        page.close()
