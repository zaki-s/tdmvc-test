


import time
from playwright.sync_api import sync_playwright

def test_add_todo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://demo.playwright.dev/todomvc")

        # logic to add a todo item
        page.fill("input.new-todo", "Beat the Elden Ring boss")
        page.press("input.new-todo", "Enter")

        # logic to check if the todo item was added
        todo_text = page.inner_text("ul.todo-list li label")
        assert todo_text == "Beat the Elden Ring boss"

        time.sleep(1)  # more seconds again to just see the work in real time
        browser.close()