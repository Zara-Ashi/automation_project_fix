import pytest
from playwright.sync_api import sync_playwright
from utils.config import URLS, VIEWPORT_MOBILE, LOGIN, PASSWORD


@pytest.fixture(scope="session")
def browser_instance():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser_instance):
    context = browser_instance.new_context()
    page = context.new_page()
    page.goto(URLS["main"])
    yield page
    context.close()


@pytest.fixture
def mobile_page(browser_instance):
    context = browser_instance.new_context(viewport=VIEWPORT_MOBILE)
    page = context.new_page()
    page.goto(URLS["main"])
    yield page
    context.close()


@pytest.fixture
def auth_page(browser_instance):
    from pages.login_page import LoginPage

    contexts = []

    def _make_auth_page(username=LOGIN, password=PASSWORD):
        context = browser_instance.new_context()
        contexts.append(context)

        page = context.new_page()
        LoginPage(page).login(username, password)

        return page

    yield _make_auth_page

    for ctx in contexts:
        ctx.close()

