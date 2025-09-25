
from playwright.sync_api import sync_playwright

def test_filter_todos():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://demo.playwright.dev/todomvc")

        # adding todo items
        todos = ["Go to hair stylist", "Beat the Elden Ring boss", "Walk my dog"]
        for todo in todos:
            page.fill("input.new-todo", todo)
            page.press("input.new-todo", "Enter")

        # marking one todo item as completed
        page.locator("ul.todo-list li").nth(1).locator(".toggle").check()

        # filtering to show only active items
        page.click("footer .filters >> text=Active")
        active_todos = page.locator("ul.todo-list li label").all_text_contents()
        assert active_todos == ["Go to hair stylist", "Walk my dog"]

        # filtering to show only completed items
        page.click("footer .filters >> text=Completed")
        completed_todos = page.locator("ul.todo-list li label").all_text_contents()
        assert completed_todos == ["Beat the Elden Ring boss"]

        browser.close()
