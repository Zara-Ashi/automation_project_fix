from pages.base_page import BasePage
from utils.config import BASE_URL


class CatalogPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.products = page.locator(".productcol, .thumbnail")
        self.product_name = page.locator(".prdocutname")
        self.price = page.locator(".price")
        self.breadcrumb = page.locator(".breadcrumb")
        self.product_img = page.locator(".thumbnail img")

    def open_category(self, path):
        self.page.goto(f"{BASE_URL}/index.php?rt=product/category&path={path}")

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
