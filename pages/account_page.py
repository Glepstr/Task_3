from pages.base_page import BasePage
from locators.account_locators import AccountLocators


class AccountPage(BasePage):

    URL = "https://qa-stellarburgers.education-services.ru/account"
    ORDER_HISTORY_URL = (
        "https://qa-stellarburgers.education-services.ru/account/order-history"
    )
    PROFILE_URL = (
        "https://qa-stellarburgers.education-services.ru/account/profile"
    )

    def open(self):
        super().open(self.URL)

    def click_order_history(self):
        self.wait_for_modals_to_disappear()
        self.click(AccountLocators.ORDER_HISTORY_LINK)

    def click_logout(self):
        self.wait_for_modals_to_disappear()
        self.click(AccountLocators.LOGOUT_BUTTON)

    def is_order_history_active(self):
        return self.find_element(
            AccountLocators.ACTIVE_ORDER_HISTORY_LINK
        ).is_displayed()

    def wait_for_order(self, order_number):
        expected_order = f"#{order_number.zfill(6)}"

        self.wait.until(
            lambda driver: expected_order in [
                element.text
                for element in driver.find_elements(
                    *AccountLocators.ORDER_NUMBERS
                )
            ]
        )