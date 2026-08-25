from pages.base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators
from utils.constants import FORGOT_PASSWORD_URL, RESET_PASSWORD_URL


class ForgotPasswordPage(BasePage):

    URL = FORGOT_PASSWORD_URL
    RESET_URL = RESET_PASSWORD_URL

    def open(self):
        super().open(self.URL)

    def enter_email(self, email):
        self.enter_text(
            ForgotPasswordLocators.EMAIL_INPUT,
            email
        )

    def click_restore(self):
        self.click(
            ForgotPasswordLocators.RESTORE_BUTTON
        )

    def enter_password(self, password):
        self.enter_text(
            ForgotPasswordLocators.PASSWORD_INPUT,
            password
        )

    def click_password_toggle(self):
        self.wait_for_modals_to_disappear()
        self.click(
            ForgotPasswordLocators.PASSWORD_TOGGLE
        )

    def enter_code(self, code):
        self.enter_text(
            ForgotPasswordLocators.CODE_INPUT,
            code
        )

    def click_save(self):
        self.click(
            ForgotPasswordLocators.SAVE_BUTTON
        )

    def click_login(self):
        self.click(
            ForgotPasswordLocators.LOGIN_LINK
        )

    def is_password_input_displayed(self):
        return self.is_element_visible(
            ForgotPasswordLocators.PASSWORD_INPUT
        )

    def is_password_active(self):
        password_container = self.find_element(
            ForgotPasswordLocators.PASSWORD_CONTAINER
        )
        return "input_status_active" in password_container.get_attribute(
            "class"
        )
