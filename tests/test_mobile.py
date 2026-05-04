import pytest
from pages.mobile_page import mobilepage


@pytest.mark.parametrize("site_url, makeup_url, product_name, device_name", [
    (
        "https://automationteststore.com",
        "product_id=50",
        "Skinsheen Bronzer Stick",
        "iPhone 14"
    )
])
def test_mob_01_mobile_navigation_to_product(browser, playwright, site_url, makeup_url, product_name, device_name):
    device = playwright.devices[device_name]
    context = browser.new_context(**device)
    page = context.new_page()
    mob = mobilepage(page)
    mob.open(site_url)
    mob.menu_btn_is_visible()
    mob.open_mobile_menu()
    mob.sidebar_is_open()
    mob.go_to_makeup()
    mob.category_page_is_opened(makeup_url)
    mob.find_product(product_name)
    context.close()