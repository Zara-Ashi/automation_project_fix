from pages.product_page import ProductPage
from pages.cart_page import CartPage
from utils.config import URLS


class TestAddToCart:

    def test_add_to_cart(self, page):
        product_page = ProductPage(page)
        page.goto(URLS["product_50"])
        product_page.add_to_cart()
        cart_page = CartPage(page)
        cart_page.open()

        assert cart_page.get_cart_count() == 1, "Количество товаров в корзине должно быть 1"

    def test_TC_CART_001_add_one_product(self, page):
        page.goto(URLS["product"])
        product_page = ProductPage(page)
        product_page.add_to_cart()
        cart_page = CartPage(page)
        cart_page.open()

        assert cart_page.get_cart_count() == 1, "Бейдж должен показывать 1 товар"

    def test_TC_CART_002_add_multiple_products(self, page):
        product_page = ProductPage(page)

        for _ in range(3):
            page.goto(URLS["product"])
            product_page.add_to_cart()

        cart_page = CartPage(page)
        cart_page.open()

        assert cart_page.get_cart_count() == 3, "Бейдж должен показывать 3 товара"

    def test_TC_CART_003_remove_product(self, page):
        product_page = ProductPage(page)
        page.goto(URLS["product"])
        product_page.add_to_cart()
        cart_page = CartPage(page)
        cart_page.open()
        cart_page.remove_first_item()

        assert cart_page.is_empty(), "Корзина должна быть пустой после удаления товара"

    def test_TC_CART_004_update_quantity(self, page):
        product_page = ProductPage(page)
        page.goto(URLS["product"])
        product_page.add_to_cart()
        cart_page = CartPage(page)
        cart_page.open()
        cart_page.update_quantity(3)

        assert cart_page.get_total() > 0, "Итоговая сумма должна быть больше 0 после обновления количества"

    def test_TC_CART_005_empty_cart_state(self, page):
        cart_page = CartPage(page)
        cart_page.open()

        assert cart_page.is_empty(), "Корзина должна быть пустой"
        assert cart_page.has_continue_button(), "Кнопка Continue должна отображаться в пустой корзине"

    def test_TC_CART_006_open_cart_from_header(self, page):
        page.goto(URLS["main"])
        cart_page = CartPage(page)
        cart_page.open_from_header()

        assert "/checkout/cart" in page.url, f"URL должен содержать /checkout/cart, получен: {page.url}"

    def test_TC_CART_007_continue_shopping(self, page):
        cart_page = CartPage(page)
        cart_page.open()
        cart_page.click_continue()

        assert URLS["main"] in page.url, f"После Continue должен быть переход на главную, получен: {page.url}"

    def test_TC_CART_008_cart_persists_after_login(self, page):
        product_page = ProductPage(page)
        page.goto(URLS["product"])
        product_page.add_to_cart()
        page.goto(URLS["login"])
        cart_page = CartPage(page)
        cart_page.open()

        assert cart_page.get_cart_count() >= 1, "Корзина должна сохраняться после перехода на страницу логина"

    def test_TC_CART_009_cart_isolated_between_users(self, auth_page):
        product_page = ProductPage(auth_page())
        cart_page = CartPage(auth_page())
        product_page.add_to_cart()
        page2 = auth_page(username="user2", password="Test1234!")
        cart_page2 = CartPage(page2)
        cart_page2.open()

        assert cart_page2.get_cart_count() == 0, "Корзина второго пользователя должна быть пустой"

    def test_TC_CART_010_total_price_calculation(self, page):
        product_page = ProductPage(page)
        page.goto(URLS["product"])
        product_page.add_to_cart()
        cart_page = CartPage(page)
        cart_page.open()
        total = cart_page.get_total()
        subtotal = cart_page.get_subtotal()

        assert abs(total - subtotal) < 0.01, f"Total {total} должен совпадать с subtotal {subtotal}"