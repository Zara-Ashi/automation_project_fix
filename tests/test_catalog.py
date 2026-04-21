from pages.catalog_page import CatalogPage
from pages.home_page import HomePage
from pages.product_page import ProductPage


def test_TC01_categories_in_menu(page):
    home = HomePage(page)
    home.open()
    sidebar = home.get_category_menu_text()

    for cat in ["MAKEUP", "SKINCARE", "FRAGRANCE", "MEN", "HAIR CARE", "BOOKS", "APPAREL"]:
        assert cat in sidebar, f"Категория '{cat}' не найдена"


def test_TC02_open_makeup_category(page):
    catalog = CatalogPage(page)
    catalog.open_category("36")

    assert "path=36" in page.url, "URL не содержит ожидаемый путь категории"
    assert catalog.get_product_count() > 0, "товары отсутствуют"


def test_TC03_open_subcategory_eyes(page):
    catalog = CatalogPage(page)
    catalog.open_category("36_39")

    assert catalog.get_product_count() > 0, "в подкатегории 'Eyes' нет товаров"


def test_TC04_product_card_has_name(page):
    catalog = CatalogPage(page)
    catalog.open_category("36")

    assert len(catalog.get_first_product_name()) > 0, "название товара пустое"


def test_TC05_product_card_has_price(page):
    catalog = CatalogPage(page)
    catalog.open_category("36")

    assert "$" in catalog.get_first_product_price(), "цена товара не содержит '$'"


def test_TC06_click_product_opens_detail(page):
    catalog = CatalogPage(page)
    catalog.open_category("36")
    catalog.click_first_product()

    assert "product/product" in page.url, "URL страницы товара не соответствует ожидаемому"


def test_TC07_product_detail_has_add_to_cart(page):
    catalog = CatalogPage(page)
    catalog.open_category("36")
    catalog.click_first_product()

    product = ProductPage(page)
    assert product.has_add_to_cart_button(), "кнопка 'Добавить в корзину' не найдена на странице товара"


def test_TC08_breadcrumb_on_category_page(page):
    catalog = CatalogPage(page)
    catalog.open_category("36")

    assert "Home" in catalog.get_breadcrumb_text(), "хлебные крошки не содержат 'Home'"


def test_TC09_search_bronzer_found(page):
    home = HomePage(page)
    home.open()
    home.search("Bronzer")

    assert "bronzer" in page.content().lower(), "результаты поиска не содержат 'bronzer'"


def test_TC10_search_not_found(page):
    home = HomePage(page)
    home.open()
    home.search("xyz999notexist")

    assert "no product" in page.content().lower(), "сообщение 'товары не найдены' не отображается"