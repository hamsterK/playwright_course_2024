from playwright.sync_api import expect


def add_task(page, field, number):
    page.locator(field).click()
    page.locator(field).fill(f"Task number {number + 1}")
    page.locator(field).press("Enter")


def test_todo(page):
    page.goto('https://demo.playwright.dev/todomvc/#/')
    expect(page).to_have_url('https://demo.playwright.dev/todomvc/#/')
    input_field = ".new-todo"
    expect(page.locator(input_field)).to_be_empty()
    for i in range(2):
        add_task(page, input_field, i)
    page.pause()  # debug
    todo_items = page.get_by_test_id('todo-item')
    expect(todo_items).to_have_count(2)
    todo_items.get_by_role('checkbox').nth(0).click()
    expect(todo_items.nth(0)).to_have_class('completed')

# set PWDEBUG=1  # enable debug mode (0 for disabling)
# set PWDEBUG=console # output debug information to the console
# pytest --headed --slowmo 1000 test_assertions_with_debug.py

# pytest --tracing=on test_assertions_with_debug.py
# pytest --tracing=retain-on-failure test_assertions_with_debug.py
# playwright show-trace test-results/test-assertions-py-test-todo-chromium/trace.zip
