from playwright.sync_api import expect

from pages.base_page import BasePage
from utils.config import URLS


class CartPage(BasePage):
    URL = URLS["cart"]

    def __init__(self, page):
        super().__init__(page)
        self.totals_table = page.locator(".cart-total")
        self.checkout_link = page.locator("a:has-text('Checkout')")

    def should_have_total(self):
        expect(self.totals_table).to_be_visible()
        expect(self.page).to_contain_text("Total")

    def proceed_to_checkout(self):
        self.checkout_link.first.click()
