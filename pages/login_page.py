import re
from pages.base_page import BasePage
from utils.config import URLS
from playwright.sync_api import expect


class LoginPage(BasePage):
    URL = URLS["login"].replace("www.", "")

    def __init__(self, page):
        super().__init__(page)
        self.username_input = page.locator("#loginFrm_loginname")
        self.password_input = page.locator("#loginFrm_password")
        self.error_alert = page.locator(".alert-danger")
        self.login_btn = page.locator("button[title='Login']")

    def open(self):
        self.page.goto(self.URL)
        expect(self.username_input).to_be_visible()

    def fill_username(self, username):
        self.username_input.fill(username)

    def fill_password(self, password):
        self.password_input.fill(password)

    def click_login(self):
        self.login_btn.click()
        expect(self.page).to_have_url(re.compile("account"), timeout=10000)

    def login(self, username, password):
        self.fill_username(username)
        self.fill_password(password)
        self.click_login()