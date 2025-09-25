from playwright.sync_api import sync_playwright

def test_filter_todos():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://demo.playwright.dev/todomvc")

        # add todos
        todos = ["Go to hair stylist", "Beat the Elden Ring boss", "Walk my dog"]
        for todo in todos:
            page.fill("input.new-todo", todo)
            page.press("input.new-todo", "Enter")

        # mark the specific todo as completed by locating the li that has that text
        todo_li = page.locator("ul.todo-list li", has_text="Beat the Elden Ring boss").first
        todo_li.locator(".toggle").click()

        # click Active filter (use the footer .filters anchor)
        page.locator("footer .filters a", has_text="Active").click()
        page.wait_for_timeout(200)  # small wait to let UI update
        active_todos = page.locator("ul.todo-list li label").all_text_contents()
        assert active_todos == ["Go to hair stylist", "Walk my dog"]

        # click Completed filter
        page.locator("footer .filters a", has_text="Completed").click()
        page.wait_for_timeout(200)
        completed_todos = page.locator("ul.todo-list li label").all_text_contents()
        assert completed_todos == ["Beat the Elden Ring boss"]

        browser.close()
