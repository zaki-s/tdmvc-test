
import time
from playwright.sync_api import sync_playwright

def test_open_todomvc():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://demo.playwright.dev/todomvc")

        assert "TodoMVC" in page.title()
        time.sleep(1) 
        browser.close() 