from pages.mobile_page import MobilePage
from pages.login_page import LoginPage
from utils.config import DEVICE_NAME, PRODUCT_NAME_SHORT, LOGIN, PASSWORD


def test_mob_01_e2e(browser, playwright):
    device = playwright.devices[DEVICE_NAME]
    context = browser.new_context(**device)
    page = context.new_page()
    mob = MobilePage(page)
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(LOGIN, PASSWORD)
    print("URL после логина:", page.url)
    mob.add_product_to_cart()
    print("URL после корзины:", page.url)
    mob.verify_cart_badge()
    mob.verify_product_in_cart(PRODUCT_NAME_SHORT)
    mob.verify_total_visible()
    mob.proceed_to_checkout()
    mob.confirm_order()
    mob.verify_success_page()
    mob.verify_order_id()
    mob.click_continue_after_order()
    mob.verify_no_horizontal_scroll()
    context.close()