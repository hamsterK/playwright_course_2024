"""
to initiate playwright recording session:
playwright codegen demo.playwright.dev/todomvc/#/
"""

import time
# from playwright.sync_api import Playwright, sync_playwright
import pytest


# def test_add_todo(playwright: Playwright)
# @pytest.mark.skip_browser('firefox')
@pytest.mark.only_browser('chromium')
def test_add_todo(page):
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()
    page.goto("https://demo.playwright.dev/todomvc/#/", wait_until='domcontentloaded')
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_label("Toggle Todo").check()
    time.sleep(2)
    # context.close()
    # browser.close()


# with sync_playwright() as playwright:
#     run(playwright)

# pytest --headed
# pytest --headed --browser webkit --browser firefox --browser chromium
# pytest --browser-channel=msedge --headed
# pytest --slowmo 1000 --headed
# pytest --device='iPhone 13 Mini' --headed
# pytest --output  # default = test-results
# pythonProject1 %  --tracing  # on / off / retain-on-failure
# pythonProject1 % pytest --video=on  # on / off / retain-on-failure
# pytest --screenshot  # on / off / retain-on-failure
# pytest --full-page-screenshot  # on / off / retain-on-failure