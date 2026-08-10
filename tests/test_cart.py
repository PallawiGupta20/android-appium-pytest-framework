import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.products_page import ProductsPage
from pages.product_details_page import ProductDetailsPage

PRODUCT_NAME = "Sauce Labs Backpack"


def test_add_product_updates_cart_badge(driver):
    products_page = ProductsPage(driver)
    products_page.open_product(PRODUCT_NAME)

    details_page = ProductDetailsPage(driver)
    details_page.add_to_cart()

    driver.back()
    assert products_page.get_cart_badge_count() == "1"
