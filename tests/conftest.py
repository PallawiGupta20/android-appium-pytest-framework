import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.fixture
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.app_package = "com.saucelabs.mydemoapp.rn"
    options.app_activity = ".MainActivity"
    options.automation_name = "UiAutomator2"
    options.no_reset = False

    drv = webdriver.Remote("http://127.0.0.1:4723", options=options)
    drv.implicitly_wait(10)

    yield drv

    drv.quit()
