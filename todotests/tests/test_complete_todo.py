

import time
from playwright.sync_api import sync_playwright

def test_complete_todo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://demo.playwright.dev/todomvc")

        # logic to add the todo item first
        page.fill("input.new-todo", "Beat the Elden Ring boss")
        page.press("input.new-todo", "Enter")

        # logic to mark it as completed
        page.check("ul.todo-list li .toggle")

        # logic to check if the todo item was marked as completed
        completed_class = page.get_attribute("ul.todo-list li", "class")
        assert "completed" in completed_class

        time.sleep(1)  # more seconds again to just see the work in real time
        browser.close()