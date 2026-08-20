from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    URL = "https://qa-stellarburgers.education-services.ru/login"

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
                    EC.visibility_of_element_located(
                        LoginLocators.ACCOUNT_LINK
                    )
                )

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

        self.wait.until(
            EC.visibility_of_element_located(
                LoginLocators.ACCOUNT_LINK
            )
        )

    def click_forgot_password(self):
        self.wait_for_modals_to_disappear()
        self.click(LoginLocators.FORGOT_PASSWORD_LINK)