BASE_URL = "https://www.automationteststore.com"

URLS = {
    "main": BASE_URL,
    "login": f"{BASE_URL}/index.php?rt=account/login",
    "checkout": f"{BASE_URL}/index.php?rt=checkout",
    "product": f"{BASE_URL}/index.php?rt=product/product&product_id=115",
    "cart": f"{BASE_URL}/index.php?rt=checkout/cart",
}
