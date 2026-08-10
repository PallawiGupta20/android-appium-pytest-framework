from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class ProductDetailsPage(BasePage):
    """Page object for an individual product's details screen."""

    ADD_TO_CART_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Add To Cart button")
    PRODUCT_PRICE = (AppiumBy.ACCESSIBILITY_ID, "product price")
    PLUS_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "counter plus button")
    MINUS_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "counter minus button")

    def add_to_cart(self):
        self.click(*self.ADD_TO_CART_BUTTON)

    def is_add_to_cart_visible(self):
        return self.is_displayed(*self.ADD_TO_CART_BUTTON)

    def get_price(self):
        return self.get_text(*self.PRODUCT_PRICE)

    def increase_quantity(self):
        self.click(*self.PLUS_BUTTON)

    def decrease_quantity(self):
        self.click(*self.MINUS_BUTTON)
