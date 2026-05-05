from playwright.sync_api import expect
from pages.base_page import BasePage
from utils.config import URLS


class CartPage(BasePage):
    URL = URLS["cart"]

    def __init__(self, page):
        super().__init__(page)
        self.product_rows = page.locator("table tbody tr")
        self.checkout_link = page.locator("a:has-text('Checkout')")
        self.continue_btn = page.locator("a[title='Continue']")
        self.qty_input = page.locator("input[name*='qty']")
        self.update_btn = page.locator("button[name='submit']")
        self.badge = page.locator(".nav.topcart span.label-orange")
        self.empty_cart_msg = page.locator("text=Your shopping cart is empty")
        self.product_name_col = page.locator("table tbody tr td:nth-child(2)")
        self.product_price_col = page.locator("table tbody tr td:nth-child(4)")
        self.product_total_col = page.locator("table tbody tr td:nth-child(6)")
        self.remove_btn = page.locator("table tbody tr td:last-child a")
        self.total_text = page.locator("text=Total")

    def open(self):
        self.page.goto(self.URL)
        expect(self.product_rows.first.or_(self.empty_cart_msg)).to_be_visible()

    def open_with_timeout(self, wait_time=1000):
        self.page.goto(self.URL)
        self.page.wait_for_timeout(wait_time)

    def should_have_product(self):
        expect(self.product_rows.first).to_be_visible()

    def get_product_name(self):
        return self.product_name_col.first.inner_text()

    def get_total(self):
        return self.product_total_col.first.inner_text().strip()

    def should_have_total(self):
        expect(self.total_text).to_be_visible()

    def proceed_to_checkout(self):
        self.checkout_link.first.click()

    def get_badge_count(self):
        expect(self.badge.first).to_be_visible()
        return int(self.badge.first.inner_text().strip())

    def is_empty(self):
        return "Your shopping cart is empty" in self.page.content()

    def has_continue_button(self):
        return self.continue_btn.count() > 0

    def remove_first_product(self):
        self.remove_btn.first.click()
        expect(self.remove_btn.first).not_to_be_visible()

    def get_first_product_price(self):
        text = self.product_price_col.first.inner_text()
        return float(text.replace("$", "").replace(",", "").strip())

    def get_first_product_qty(self):
        return float(self.qty_input.first.input_value())

    def get_subtotal(self):
        text = self.product_total_col.first.inner_text()
        return float(text.replace("$", "").replace(",", "").strip())

    def update_qty(self, qty):
        self.qty_input.first.fill(str(qty))
        self.update_btn.first.click()
        expect(self.qty_input.first).to_have_value(str(qty))

    def click_continue(self):
        self.continue_btn.click()
        expect(self.page).to_have_url(URLS["main"])