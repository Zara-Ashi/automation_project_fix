from pages.base_page import BasePage
from utils.config import BASE_URL
from playwright.sync_api import expect

class CatalogPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.products = page.locator(".productcol, .thumbnail")
        self.product_name = page.locator(".prdocutname")
        self.price = page.locator(".price")
        self.breadcrumb = page.locator(".breadcrumb")
        self.product_img = page.locator(".thumbnail img")

        self.add_to_cart_buttons = page.locator("a[title='Add to Cart']")
        self.cart_badge = page.locator(".nav.topcart span.label-orange")
        self.product_submit_button = page.locator("button[type='submit']")
        self.product_cart_button = page.locator("a.productcart")
        self.product_cart_with_id = page.locator("a.productcart[data-id]")

    def open_category(self, category_id):
        self.page.goto(f"https://automationteststore.com/index.php?rt=product/category&path={category_id}")

    def open_category_sorted(self, path, sort):
        self.page.goto(f"{BASE_URL}/index.php?rt=product/category&path={path}&sort={sort}")

    def get_product_count(self):
        return self.products.count()

    def get_first_product_name(self):
        return self.product_name.first.inner_text()

    def get_first_product_price(self):
        return self.price.first.inner_text()

    def click_first_product(self):
        self.product_name.first.click()
        self.page.wait_for_load_state("networkidle")

    def get_breadcrumb_text(self):
        return self.breadcrumb.inner_text()

    def get_first_image_natural_width(self):
        return self.product_img.first.evaluate("el => el.naturalWidth")

    def add_first_product_to_cart(self):
        count = self.add_to_cart_buttons.count()
        assert count > 0, "Нет кнопок Add to Cart"

        for i in range(count):
            btn = self.add_to_cart_buttons.nth(i)

            if btn.count() == 0:
                continue

            if not btn.is_visible():
                continue

            btn.scroll_into_view_if_needed()

            if not btn.is_enabled():
                continue

            btn.click()

            if "subscriber" in self.page.url:
                self.page.go_back()
                continue

            if "product_id" in self.page.url:
                if self.product_submit_button.count() > 0 and self.product_submit_button.first.is_enabled():
                    self.product_submit_button.first.click()

            if self.cart_badge.count() > 0 and self.cart_badge.inner_text() != "0":
                return

            self.page.go_back()

        raise Exception("Не удалось добавить ни один товар")

    def add_product_to_cart(self, index):
        self.page.goto(f"{BASE_URL}/index.php?rt=product/category&path=36")
        self.page.wait_for_timeout(1000)

        product_id = self.product_cart_with_id.nth(index).get_attribute("data-id")

        if product_id:
            self.page.evaluate(f"update_cart({product_id})")
            self.page.wait_for_timeout(2000)
        else:
            self.product_cart_button.nth(index).click()
            self.page.wait_for_timeout(2000)