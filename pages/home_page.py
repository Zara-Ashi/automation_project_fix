from pages.base_page import BasePage
from utils.config import BASE_URL


class HomePage(BasePage):
    URL = BASE_URL

    def __init__(self, page):
        super().__init__(page)
        self.search_input = page.locator("#filter_keyword")
        self.search_button = page.locator(".button-in-search")
        self.category_menu = page.locator("#categorymenu")

    def get_category_menu_text(self):
        return self.category_menu.inner_text().upper()

    def search(self, keyword):
        self.search_input.fill(keyword)
        self.search_button.click()
        self.page.wait_for_load_state("networkidle")
