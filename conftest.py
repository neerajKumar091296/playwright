'''
Docstring for conftest

This file should be named as conftest.py. This will capture the repeating code

'''


import pytest

from playwright.sync_api import  sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser # Generator function
        browser.close()

@pytest.fixture()
def page(browser):
    page = browser.new_page()
    yield page
    page.close()