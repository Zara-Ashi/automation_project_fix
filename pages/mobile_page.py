import re
from playwright.sync_api import Page, expect
from utils.config import URLS


class MobilePage:

    def __init__(self, page: Page):
        self.page = page
        self.menu_btn = page.locator(".navbar-toggle")
        self.sidebar = page.locator("#categorymenu")
        self.cart_badge = page.locator(".nav.topcart span.label-orange")
        self.products = page.locator(".productcol, .thumbnail")

    def open(self):
        self.page.goto(URLS["main"])

    def menu_btn_is_visible(self):
        expect(self.menu_btn).to_be_visible()

    def open_mobile_menu(self):
        self.menu_btn.click()
        expect(self.sidebar).to_be_visible()

    def sidebar_is_open(self):
        expect(self.sidebar).to_be_visible()

    def add_product_to_cart(self):
        self.page.goto(URLS["product"].replace("www.", ""))
        self.page.wait_for_load_state("domcontentloaded")
        self.page.locator("a.cart").click()
        expect(self.page).to_have_url(re.compile("checkout/cart"), timeout=10000)

    def verify_cart_badge(self):
        expect(self.cart_badge.first).not_to_have_text("0")

    def verify_product_in_cart(self, name):
        expect(self.page.get_by_text(name, exact=False).first).to_be_attached()

    def verify_total_visible(self):
        expect(self.page.get_by_text("Sub-Total").first).to_be_attached()

    def proceed_to_checkout(self):
        self.page.goto(URLS["checkout_shipping"])
        self.page.wait_for_load_state("domcontentloaded")
        print("URL после shipping:", self.page.url)

    def confirm_order(self):
        self.page.locator("button.btn-orange, button[name='confirm']").first.click()
        expect(self.page).to_have_url(re.compile("checkout/success"))

    def verify_success_page(self):
        expect(self.page.get_by_role("heading", level=1)).to_contain_text("Processed")

    def verify_order_id(self):
        pass

    def click_continue_after_order(self):
        self.page.get_by_role("link", name="Continue").click()
        expect(self.page).to_have_url(re.compile(r"automationteststore\.com"))

    def verify_no_horizontal_scroll(self):
        result = self.page.evaluate("() => document.body.scrollWidth <= window.innerWidth")
        assert result, "Есть горизонтальный скролл"