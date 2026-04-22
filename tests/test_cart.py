from pages.product_page import ProductPage
from pages.cart_page import CartPage


class TestAddToCart:
    def test_add_to_cart(self, page):
        product_page = ProductPage(page)
        cart_page = CartPage(page)

        page.goto(page.base_url + "/index.php?rt=product/product&product_id=50")

        product_page.add_to_cart()
        cart_page.open()
        cart_page.should_have_product()
        cart_page.should_have_total()

        assert cart_page.get_product_name() != ""