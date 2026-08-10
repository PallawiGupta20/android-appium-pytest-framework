from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class CartPage(BasePage):
    """Page object for the cart screen."""

    def get_cart_items(self):
        return self.find_elements(AppiumBy.XPATH, '//android.widget.TextView')
