from pages.base_page import BasePage
from utils.config import BASE_URL
from playwright.sync_api import expect

class LoginPage(BasePage):
    URL = f"{BASE_URL}/index.php?rt=account/login"

    def __init__(self, page):
        super().__init__(page)
        self.username_input = page.locator("#loginFrm_loginname")
        self.password_input = page.locator("#loginFrm_password")
        self.login_btn = page.get_by_role("button", name="Login")
        self.error_alert = page.locator(".alert-danger")

    def open(self):
        self.page.goto(self.URL)
        self.page.wait_for_selector("#loginFrm_loginname")

    def fill_username(self, username):
        self.username_input.fill(username)

    def fill_password(self, password):
        self.password_input.fill(password)

    def click_login(self):
        with self.page.expect_navigation(wait_until="networkidle"):
            self.page.get_by_role("button", name="Login").click()

    def login(self, username, password):
        self.fill_username(username)
        self.fill_password(password)
        self.click_login()
        expect(self.page).to_have_url(
            lambda url: "account" in url, timeout=10000
        )
