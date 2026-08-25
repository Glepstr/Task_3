import allure

from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.constructor_page import ConstructorPage


class TestAccount:

    @allure.title("Переход в личный кабинет")
    def test_open_personal_account(self, driver, test_user):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        login_page.open()
        login_page.login(
            test_user["email"],
            test_user["password"]
        )

        main_page.click_personal_account()

        assert account_page.is_order_history_link_displayed()

    @allure.title("Переход в историю заказов")
    def test_open_order_history(self, driver, test_user):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        login_page.open()
        login_page.login(
            test_user["email"],
            test_user["password"]
        )

        main_page.click_personal_account()
        account_page.click_order_history()

        assert account_page.is_order_history_active()

    @allure.title("Выход из аккаунта")
    def test_logout(self, driver, test_user):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        login_page.open()
        login_page.login(
            test_user["email"],
            test_user["password"]
        )

        main_page.click_personal_account()
        account_page.click_logout()

        assert login_page.is_login_button_displayed()

    @allure.title("Созданный заказ отображается в истории заказов")
    def test_created_order_appears_in_history(self, driver, test_user):
        login_page = LoginPage(driver)
        constructor_page = ConstructorPage(driver)
        account_page = AccountPage(driver)

        login_page.open()
        login_page.login(
            test_user["email"],
            test_user["password"]
        )

        constructor_page.drag_bun_to_basket()
        constructor_page.click_order()

        order_number = constructor_page.get_order_number()

        account_page.open()
        account_page.click_order_history()

        assert account_page.wait_for_order(order_number)
