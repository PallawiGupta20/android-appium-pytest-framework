import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.products_page import ProductsPage

PRODUCT_NAME = "Sauce Labs Backpack"


def test_app_launches(driver):
    assert driver.current_package == "com.saucelabs.mydemoapp.rn"


def test_product_list_visible(driver):
    products_page = ProductsPage(driver)
    assert products_page.is_product_visible(PRODUCT_NAME)
