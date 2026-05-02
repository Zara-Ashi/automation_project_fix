BASE_URL = "https://automationteststore.com"

URLS = {
    "main":         f"{BASE_URL}",
    "login":        f"{BASE_URL}/index.php?rt=account/login",
    "checkout":     f"{BASE_URL}/index.php?rt=checkout",
    "product":      f"{BASE_URL}/index.php?rt=product/product&product_id=115",
    "cart":         f"{BASE_URL}/index.php?rt=checkout/cart",
    "registration": f"{BASE_URL}/index.php?rt=account/create",
}

VIEWPORT_MOBILE = {"width": 375, "height": 667}

LOGIN    = "autotester_user"
PASSWORD = "Test1234!"