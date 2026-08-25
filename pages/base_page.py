from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.base_locators import BaseLocators


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

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text

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
        return self.wait.until(
            lambda driver: any(
                element.is_displayed()
                for element in self.find_elements(locator)
            )
        )

    def wait_for_element_to_disappear(self, locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator)
        )

    def get_browser_name(self):
        return self.driver.name

    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    def drag_and_drop(self, source, target):
        ActionChains(self.driver).drag_and_drop(
            source,
            target
        ).perform()