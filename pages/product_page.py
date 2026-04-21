from pages.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.add_to_cart_btn = page.locator("button[title='Add to Cart'], .btn-orange")
        self.add_to_cart_text = page.locator("text=Add to Cart")

    def add_to_cart(self):
        self.add_to_cart_text.first.click()

    def has_add_to_cart_button(self):
        return self.add_to_cart_btn.count() > 0

    def has_images(self):
        return self.page.locator("img").count() > 0
