import re
from playwright.sync_api import Page, expect


class mobilepage:

    def __init__(self, page: Page):
        self.page        = page
        self.menu_btn    = page.locator(".navbar-toggle")
        self.sidebar     = page.locator("#categorymenu")
        self.product_links = page.locator("a")

    def open(self, url):
        self.page.goto(url)

    def menu_btn_is_visible(self):
        expect(self.menu_btn).to_be_visible()

    def open_mobile_menu(self):
        self.menu_btn.click()
        self.page.wait_for_timeout(1000)

    def sidebar_is_open(self):
        expect(self.sidebar).to_be_visible()

    def go_to_makeup(self):
        self.page.goto("https://automationteststore.com/index.php?rt=product/product&product_id=50")

    def category_page_is_opened(self, url_part):
        expect(self.page).to_have_url(re.compile(url_part))

    def find_product(self, name):
        self.page.wait_for_load_state("networkidle")
        product = self.product_links.filter(has_text=name).first
        expect(product).to_be_visible(timeout=10000)