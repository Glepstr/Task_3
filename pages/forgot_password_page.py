from pages.base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators


class ForgotPasswordPage(BasePage):

    URL = "https://qa-stellarburgers.education-services.ru/forgot-password"
    RESET_URL = "https://qa-stellarburgers.education-services.ru/reset-password"

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

    def click_password_toggle(self):
        self.wait_for_modals_to_disappear()

        self.click(
            ForgotPasswordLocators.PASSWORD_TOGGLE
        )

    def is_password_active(self):
        password_container = self.find_element(
            ForgotPasswordLocators.PASSWORD_CONTAINER
        )

        return "input_status_active" in password_container.get_attribute(
            "class"
       )