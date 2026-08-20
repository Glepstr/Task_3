from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.base_locators import BaseLocators
from locators.constructor_locators import ConstructorLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_modals_to_disappear(self):
        self.wait.until(
            lambda driver: all(
                not overlay.is_displayed()
                for overlay in driver.find_elements(
                    *BaseLocators.MODAL_OVERLAYS
                )
            )
        )

    def is_element_visible(self, locator):
        return any(
            element.is_displayed()
            for element in self.driver.find_elements(*locator)
        )

    def wait_for_element_to_disappear(self, locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator)
        )