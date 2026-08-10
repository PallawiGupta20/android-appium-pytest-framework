import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.products_page import ProductsPage
from pages.product_details_page import ProductDetailsPage

PRODUCT_NAME = "Sauce Labs Backpack"


def test_open_product_details(driver):
    products_page = ProductsPage(driver)
    products_page.open_product(PRODUCT_NAME)

    details_page = ProductDetailsPage(driver)
    assert details_page.is_add_to_cart_visible()


def test_product_price_displayed(driver):
    products_page = ProductsPage(driver)
    products_page.open_product(PRODUCT_NAME)

    details_page = ProductDetailsPage(driver)
    price = details_page.get_price()
    assert price.startswith("$")
