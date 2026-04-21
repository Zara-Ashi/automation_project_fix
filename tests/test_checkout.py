from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.product_page import ProductPage
from utils.config import URLS


def test_TC01_checkout_order(page):
    page.goto(URLS["product"])
    product_page = ProductPage(page)
    product_page.add_to_cart()

    cart_page = CartPage(page)
    cart_page.open()
    cart_page.should_have_total()
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(page)
    checkout_page.select_guest_checkout()
    checkout_page.fill_guest_form(
        first_name="Test",
        last_name="User",
        email="testuser@example.com",
        address="Street 1",
        city="Dushanbe",
        country="Tajikistan",
        postcode="734000",
    )
    checkout_page.confirm_order()
    checkout_page.should_show_checkout_confirmation()
