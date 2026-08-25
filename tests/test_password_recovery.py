import allure

from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage


class TestPasswordRecovery:

    @allure.title("Переход на страницу восстановления пароля")
    def test_open_password_recovery_page(self, driver):
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)

        login_page.open()
        login_page.click_forgot_password()

        assert forgot_password_page.get_current_url() ==             ForgotPasswordPage.URL

    @allure.title("Ввод email и переход к форме восстановления пароля")
    def test_password_recovery_form(self, driver, test_user):
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)

        login_page.open()
        login_page.click_forgot_password()

        forgot_password_page.enter_email(
            test_user["email"]
        )
        forgot_password_page.click_restore()

        assert forgot_password_page.is_password_input_displayed()

    @allure.title("Поле пароля подсвечивается после клика на глазик")
    def test_password_field_becomes_active(self, driver, test_user):
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)

        login_page.open()
        login_page.click_forgot_password()

        forgot_password_page.enter_email(
            test_user["email"]
        )
        forgot_password_page.click_restore()

        forgot_password_page.click_password_toggle()

        assert forgot_password_page.is_password_active()
