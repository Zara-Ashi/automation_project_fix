BASE_URL = "https://www.automationteststore.com"

CATEGORY_URL = BASE_URL + "/index.php?rt=product/category&path={}"

URLS = {
    "main": BASE_URL,
    "login": f"{BASE_URL}/index.php?rt=account/login",
    "checkout": f"{BASE_URL}/index.php?rt=checkout",
    "checkout_shipping": "https://automationteststore.com/index.php?rt=checkout/shipping",
    "product": f"{BASE_URL}/index.php?rt=product/product&product_id=115",
    "product_50": f"{BASE_URL}/index.php?rt=product/product&product_id=50",
    "cart": f"{BASE_URL}/index.php?rt=checkout/cart",
    "registration": f"{BASE_URL}/index.php?rt=account/create",
    "category_36": CATEGORY_URL.format(36),
    "login_no_www": "https://automationteststore.com/index.php?rt=account/login",
}

GUEST_DATA = ("Zara", "Ashi", "ashi@test.com", "Amirshoev 12",
              "Dushanbe", "Tajikistan", "735700")
DEFAULT_PASSWORD = "Test1234!"
DEVICE_NAME = "iPhone 14"
PRODUCT_NAME = "Tropiques Minerale Loose Bronzer"
PRODUCT_NAME_SHORT = "Fiorella"
CATEGORY_URL_PART = "rt=product/category"
VIEWPORT_MOBILE = {"width": 390, "height": 844}
LOGIN = "zaza_jura"
PASSWORD = "Zara9559!"
