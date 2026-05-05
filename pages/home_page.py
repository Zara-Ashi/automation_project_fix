from pages.base_page import BasePage
from utils.config import BASE_URL, URLS
from playwright.sync_api import expect


class HomePage(BasePage):
    URL = BASE_URL

    def __init__(self, page):
        super().__init__(page)
        self.search_input = page.locator("#filter_keyword")
        self.search_button = page.locator(".button-in-search")
        self.category_menu = page.locator("#categorymenu")
        self.page_body = page.locator("body")

    def get_category_menu_text(self):
        return self.category_menu.inner_text().upper()

    def search(self, keyword):
        self.search_input.fill(keyword)
        self.search_button.click()
        expect(self.search_input).to_be_visible(timeout=10000)

    def open(self):
        self.page.goto(self.URL)
        expect(self.category_menu).to_be_visible()

    def open_with_timeout(self, wait_time=1000):
        self.page.goto(self.URL)
        self.page.wait_for_timeout(wait_time)