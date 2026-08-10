class BasePage:
    """Shared functionality for all page objects."""

    def __init__(self, driver):
        self.driver = driver

    def click(self, by, value):
        self.driver.find_element(by, value).click()

    def get_text(self, by, value):
        return self.driver.find_element(by, value).text

    def is_displayed(self, by, value):
        try:
            return self.driver.find_element(by, value).is_displayed()
        except Exception:
            return False

    def find_elements(self, by, value):
        return self.driver.find_elements(by, value)
