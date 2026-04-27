from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.product_page import ProductPage
from utils.config import URLS

def test_TC_CHECKOUT_001(page):
    page.goto(URLS["product"])
    product_page = ProductPage(page)
    product_page.add_to_cart()
    cart_page = CartPage(page)
    cart_page.open()
    cart_page.proceed_to_checkout()
    checkout_page = CheckoutPage(page)
    checkout_page.select_guest_checkout()
    checkout_page.fill_guest_form("Zara","Ashi","ashi@test.com","Amirshoev 12","Dushanbe","Tajikistan","735700")
    checkout_page.confirm_order()
    checkout_page.verify_checkout_confirmation()

def test_TC_CHECKOUT_002(page):
    page.goto(URLS["product"])
    ProductPage(page).add_to_cart()
    cart_page = CartPage(page)
    cart_page.open()
    cart_page.proceed_to_checkout()
    checkout_page = CheckoutPage(page)
    checkout_page.verify_guest_option()
    checkout_page.verify_returning_customer_option()

def test_TC_CHECKOUT_003(page):
    page.goto(URLS["product"])
    ProductPage(page).add_to_cart()
    cart_page = CartPage(page)
    cart_page.open()
    cart_page.proceed_to_checkout()
    checkout_page = CheckoutPage(page)
    checkout_page.select_guest_checkout()
    checkout_page.confirm_order()
    checkout_page.verify_validation_errors()

def test_TC_CHECKOUT_004(page):
    page.goto(URLS["product"])
    ProductPage(page).add_to_cart()
    cart_page = CartPage(page)
    cart_page.open()
    cart_page.proceed_to_checkout()
    checkout_page = CheckoutPage(page)
    checkout_page.select_guest_checkout()
    checkout_page.fill_guest_form("Zara","Ashi","ashi@test.com","Amirshoev 12","Dushanbe","Tajikistan","735700")
    checkout_page.confirm_order()
    checkout_page.verify_email_error()

def test_TC_CHECKOUT_005(page):
    page.goto(URLS["product"])
    ProductPage(page).add_to_cart()
    cart_page = CartPage(page)
    cart_page.open()
    cart_page.proceed_to_checkout()
    checkout_page = CheckoutPage(page)
    checkout_page.select_country("Germany")
    checkout_page.verify_regions_updated()

def test_TC_CHECKOUT_006(page):
    page.goto(URLS["product"])
    ProductPage(page).add_to_cart()
    cart_page = CartPage(page)
    cart_page.open()
    cart_page.proceed_to_checkout()
    page.go_back()
    cart_page = CartPage(page)
    cart_page.verify_not_empty()

def test_TC_CHECKOUT_007(page):
    page.goto(URLS["product"])
    ProductPage(page).add_to_cart()
    cart_page = CartPage(page)
    cart_page.open()
    cart_page.proceed_to_checkout()
    checkout_page = CheckoutPage(page)
    checkout_page.select_guest_checkout()
    checkout_page.fill_guest_form("Zara","Ashi","ashi@test.com","Amirshoev 12","Dushanbe","Tajikistan","735700")
    checkout_page.confirm_order()
    checkout_page.verify_success_url()
    checkout_page.verify_order_number()

def test_TC_CHECKOUT_008(page):
    page.goto(URLS["product"])
    ProductPage(page).add_to_cart()
    cart_page = CartPage(page)
    cart_page.open()
    cart_page.proceed_to_checkout()
    checkout_page = CheckoutPage(page)
    checkout_page.select_guest_checkout()
    checkout_page.fill_guest_form("Zara","Ashi","ashi@test.com","Amirshoev 12","Dushanbe","Tajikistan","735700")
    total = checkout_page.get_total()
    expected = checkout_page.get_subtotal() + checkout_page.get_tax() + checkout_page.get_shipping()
    assert abs(total - expected) < 0.01

def test_TC_CHECKOUT_009(page):
    page.goto(URLS["product"])
    ProductPage(page).add_to_cart()
    cart_page = CartPage(page)
    cart_page.open()
    cart_page.proceed_to_checkout()
    checkout_page = CheckoutPage(page)
    total = checkout_page.get_total()
    assert round(total, 2) == total

def test_TC_CHECKOUT_010(page):
    page.goto(URLS["product"])
    product_page = ProductPage(page)
    product_page.add_to_cart()
    page.goto(URLS["product"])
    product_page.add_to_cart()
    cart_page = CartPage(page)
    cart_page.open()
    cart_page.proceed_to_checkout()
    checkout_page = CheckoutPage(page)
    checkout_page.select_guest_checkout()
    checkout_page.fill_guest_form("Zara","Ashi","ashi@test.com","Amirshoev 12","Dushanbe","Tajikistan","735700")
    checkout_page.confirm_order()
    checkout_page.verify_order_number()
    assert checkout_page.get_total() > 0