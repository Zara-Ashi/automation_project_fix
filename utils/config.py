BASE_URL = "https://automationteststore.com"

URLS = {
    "main": BASE_URL,
    "login": f"{BASE_URL}/index.php?rt=account/login",
    "checkout": f"{BASE_URL}/index.php?rt=checkout",
    "product": f"{BASE_URL}/index.php?rt=product/product&product_id=115",
    "product_50": f"{BASE_URL}/index.php?rt=product/product&product_id=50",
    "cart": f"{BASE_URL}/index.php?rt=checkout/cart",
    "registration": f"{BASE_URL}/index.php?rt=account/create",
}

GUEST_DATA = ("Zara", "Ashi", "ashi@test.com", "Amirshoev 12",
              "Dushanbe", "Tajikistan", "735700")
DEFAULT_PASSWORD = "Test1234!"
