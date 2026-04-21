import pytest
from playwright.sync_api import sync_playwright

from utils.config import BASE_URL

LOGIN = "autotester_user"
PASSWORD = "Test1234!"


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
    page.goto(BASE_URL)
    yield page
    context.close()


@pytest.fixture
def mobile_page(browser_instance):
    context = browser_instance.new_context(viewport={"width": 375, "height": 667})
    page = context.new_page()
    page.goto(BASE_URL)
    yield page
    context.close()


@pytest.fixture
def auth_page(browser_instance):
    """Factory fixture. Returns a callable: auth_page() for default user,
    auth_page(username="other", password="pass") for any other user."""
    contexts = []

    def _make_auth_page(username=LOGIN, password=PASSWORD):
        from pages.login_page import LoginPage
        context = browser_instance.new_context()
        contexts.append(context)
        p = context.new_page()
        login_page = LoginPage(p)
        login_page.open()
        login_page.login(username, password)
        return p

    yield _make_auth_page

    for ctx in contexts:
        ctx.close()