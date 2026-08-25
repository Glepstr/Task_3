from pages.base_page import BasePage
from locators.main_locators import MainLocators
from utils.constants import CONSTRUCTOR_URL


class MainPage(BasePage):

    URL = CONSTRUCTOR_URL

    def open(self):
        super().open(self.URL)

    def click_personal_account(self):
        self.wait_for_modals_to_disappear()
        self.click(MainLocators.PERSONAL_ACCOUNT_LINK)
