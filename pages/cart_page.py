from playwright.sync_api import expect
from pages.base_page import BasePage
from utils.config import URLS


class CartPage(BasePage):
    URL = URLS["cart"]

    def __init__(self, page):
        super().__init__(page)
        self.product_rows = page.locator("table tbody tr")
        self.checkout_link = page.locator("a:has-text('Checkout')")

    def open(self):
        self.page.goto(self.URL)
        expect(self.page).to_have_url(self.URL)

    def should_have_product(self):
        expect(self.product_rows.first).to_be_visible()

    def get_product_name(self):
        return self.page.locator("table tbody tr td:nth-child(2)").first.inner_text()

    def get_total(self):
        total = self.page.locator("table tbody tr td:nth-child(6)").first.inner_text()
        return total.strip()

    def should_have_total(self):
        expect(self.page.locator("text=Total")).to_be_visible()

    def proceed_to_checkout(self):
        self.checkout_link.first.click()