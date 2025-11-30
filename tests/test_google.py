
import re
from playwright.sync_api import  expect


def test_google_page(page):
    page.wait_for_timeout(4000)
    page.goto("https://www.google.com/")
    page.get_by_role("combobox",name = "search").fill("playwright Python")
    page.keyboard.press("Enter")
    expect(page).to_have_title(re.compile("Playwright",re.IGNORECASE))









