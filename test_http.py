import time
from playwright.sync_api import Page


def test_listen_network(page: Page):
    page.on("request", lambda request: print(">>", request.method, request.url))
    page.on("response", lambda response: print("<<", response.status, response.url))
    page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())  # abort if image
    page.goto('https://www.google.com')


def test_edit_request(page):
    page.route("**/register", lambda route: route.continue_(post_data='{"email": "user","password": "secret"}'))
    page.goto('https://reqres.in/')
    page.get_by_text(' Register - successful ').click()
    time.sleep(2)


def test_edit_response(page):
    page.route("**/api/tags", lambda route: route.fulfill(path="data.json"))
    page.goto('https://demo.realworld.io/')
    time.sleep(2)

