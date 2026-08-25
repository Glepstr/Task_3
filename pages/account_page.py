from pages.base_page import BasePage
from locators.account_locators import AccountLocators
from utils.constants import ACCOUNT_URL, ORDER_HISTORY_URL, PROFILE_URL


class AccountPage(BasePage):

    URL = ACCOUNT_URL
    ORDER_HISTORY_URL = ORDER_HISTORY_URL
    PROFILE_URL = PROFILE_URL

    def open(self):
        super().open(self.URL)

    def click_order_history(self):
        self.wait_for_modals_to_disappear()
        self.click(AccountLocators.ORDER_HISTORY_LINK)

    def click_logout(self):
        self.wait_for_modals_to_disappear()
        self.click(AccountLocators.LOGOUT_BUTTON)

    def is_order_history_link_displayed(self):
        return self.is_element_visible(
            AccountLocators.ORDER_HISTORY_LINK
        )

    def is_order_history_active(self):
        return self.is_element_visible(
            AccountLocators.ACTIVE_ORDER_HISTORY_LINK
        )

    def wait_for_order(self, order_number):
        expected_order = f"#{order_number.zfill(6)}"

        self.wait.until(
            lambda driver: expected_order in [
                element.text
                for element in self.find_elements(
                    AccountLocators.ORDER_NUMBERS
                )
            ]
        )
        return True