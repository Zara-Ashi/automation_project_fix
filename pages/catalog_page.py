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
        badge = self.page.locator(".nav.topcart span.label-orange")
        buttons = self.page.locator("a[title='Add to Cart']")

        count = buttons.count()
        assert count > 0, "Нет кнопок Add to Cart"

        for i in range(count):
            btn = buttons.nth(i)

            try:
                # 👇 прокрутка к элементу
                btn.scroll_into_view_if_needed()

                # 👇 ждём, пока станет кликабельной
                expect(btn).to_be_visible(timeout=3000)

                btn.click(timeout=3000)

            except:
                continue

            # редирект на подписку → пропускаем
            if "subscriber" in self.page.url:
                self.page.go_back()
                continue

            # если попали в товар
            if "product_id" in self.page.url:
                product_button = self.page.locator("button[type='submit']")
                if product_button.count() > 0:
                    product_button.click()

            # проверяем корзину
            try:
                expect(badge).not_to_have_text("0", timeout=3000)
                return
            except:
                self.page.go_back()

        raise Exception("Не удалось добавить ни один товар")

    def add_product_to_cart(self, index):
        self.page.goto(f"{BASE_URL}/index.php?rt=product/category&path=36")
        self.page.wait_for_timeout(1000)
        product_id = self.page.locator("a.productcart[data-id]").nth(index).get_attribute("data-id")
        if product_id:
            self.page.evaluate(f"update_cart({product_id})")
            self.page.wait_for_timeout(2000)
        else:
            self.page.locator("a.productcart").nth(index).click()
            self.page.wait_for_timeout(2000)