from pages.product_page import ProductPage
from pages.cart_page import CartPage
from utils.config import URLS


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


    def test_TC_CART_001_add_one_product(page):
        page.goto(URLS["product"])

        product_page = ProductPage(page)
        cart_page = CartPage(page)

        product_page.add_to_cart()

        cart_page.open()

        assert cart_page.get_cart_count() == 1

    def test_TC_CART_002_add_multiple_products(page):
        product_page = ProductPage(page)
        cart_page = CartPage(page)

        for _ in range(3):
            page.goto(URLS["product"])
            product_page.add_to_cart()

        cart_page.open()

        assert cart_page.get_cart_count() == 3

    def test_TC_CART_003_remove_product(page):
        product_page = ProductPage(page)
        cart_page = CartPage(page)

        page.goto(URLS["product"])
        product_page.add_to_cart()

        cart_page.open()
        cart_page.remove_first_item()

        assert cart_page.is_empty()

    def test_TC_CART_004_update_quantity(page):
        product_page = ProductPage(page)
        cart_page = CartPage(page)

        page.goto(URLS["product"])
        product_page.add_to_cart()

        cart_page.open()
        cart_page.update_quantity(3)

        assert cart_page.get_total() > 0

    def test_TC_CART_005_empty_cart_state(page):
        cart_page = CartPage(page)

        cart_page.open()

        assert cart_page.is_empty()
        assert cart_page.has_continue_button()

    def test_TC_CART_006_open_cart_from_header(page):
        page.goto(URLS["main"])

        cart_page = CartPage(page)
        cart_page.open_from_header()

        assert "/checkout/cart" in page.url

    def test_TC_CART_007_continue_shopping(page):
        cart_page = CartPage(page)

        cart_page.open()
        cart_page.click_continue()

        assert URLS["main"] in page.url

    def test_TC_CART_008_cart_persists_after_login(page):
        product_page = ProductPage(page)
        cart_page = CartPage(page)

        page.goto(URLS["product"])
        product_page.add_to_cart()

        page.goto(URLS["login"])

        cart_page.open()

        assert cart_page.get_cart_count() >= 1

    def test_TC_CART_009_cart_isolated_between_users(auth_page):
        product_page = ProductPage(auth_page())
        cart_page = CartPage(auth_page())

        product_page.add_to_cart()

        page2 = auth_page(username="user2", password="Test1234!")

        cart_page2 = CartPage(page2)
        cart_page2.open()

        assert cart_page2.get_cart_count() == 0

    def test_TC_CART_010_total_price_calculation(page):
        product_page = ProductPage(page)
        cart_page = CartPage(page)

        page.goto(URLS["product"])
        product_page.add_to_cart()

        cart_page.open()

        total = cart_page.get_total()
        subtotal = cart_page.get_subtotal()

        assert abs(total - subtotal) < 0.01