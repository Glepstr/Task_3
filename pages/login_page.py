from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from utils.constants import LOGIN_URL


class LoginPage(BasePage):

    URL = LOGIN_URL

    def open(self):
        super().open(self.URL)

    def enter_email(self, email):
        self.enter_text(LoginLocators.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.enter_text(LoginLocators.PASSWORD_INPUT, password)

    def click_login(self):
        self.wait_for_modals_to_disappear()
        self.click(LoginLocators.LOGIN_BUTTON)
        self.wait.until(
            lambda driver: self.is_element_visible(
                LoginLocators.ACCOUNT_LINK
            )
        )

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def click_forgot_password(self):
        self.wait_for_modals_to_disappear()
        self.click(LoginLocators.FORGOT_PASSWORD_LINK)

    def click_password_visibility(self):
        self.click(LoginLocators.PASSWORD_VISIBILITY_BUTTON)

    def is_login_button_displayed(self):
        return self.is_element_visible(
            LoginLocators.LOGIN_BUTTON
        )
