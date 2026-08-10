from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class ProductsPage(BasePage):
    """Page object for the product catalog / home screen."""

    def product_locator(self, product_name):
        return AppiumBy.XPATH, f'//android.widget.TextView[@text="{product_name}"]'

    def is_product_visible(self, product_name):
        by, value = self.product_locator(product_name)
        return len(self.find_elements(by, value)) > 0

    def open_product(self, product_name):
        by, value = self.product_locator(product_name)
        self.click(by, value)

    def open_cart(self):
        self.click(AppiumBy.XPATH, '//android.view.ViewGroup[contains(@content-desc, "cart")]')

    def get_cart_badge_count(self):
        return self.get_text(
            AppiumBy.XPATH,
            '//android.view.ViewGroup[contains(@content-desc, "cart")]//android.widget.TextView',
        )
