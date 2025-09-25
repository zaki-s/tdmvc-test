
import time
from playwright.sync_api import sync_playwright

def test_delete_todo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://demo.playwright.dev/todomvc")
        
        # add item
        page.fill("input.new-todo", "Beat the Elden Ring boss")
        page.press("input.new-todo", "Enter")

        # delete item
        todo_item = page.locator("ul.todo-list li").nth(0)
        todo_item.hover()
        todo_item.locator(".destroy").click()

        # verify item is deleted
        todo_count = page.locator("ul.todo-list li").count()
        assert todo_count == 0

        time.sleep(1)
        browser.close()