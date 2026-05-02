from playwright.sync_api import expect
from pages.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.add_to_cart_btn_first = page.locator(
            "button[title='Add to Cart'], .cart, .btn-cart, .btn-orange"
        ).first
        self.images = page.locator("img")

    def add_to_cart(self):
        expect(self.add_to_cart_btn.first).to_be_visible(timeout=10000)
        self.add_to_cart_btn.first.click()

    def has_add_to_cart_button(self):
        return self.add_to_cart_btn.count() > 0

    def has_images(self):
        return self.images.count() > 0