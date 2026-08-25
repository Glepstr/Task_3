import allure

from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage


class TestConstructor:

    @allure.title("Переход в конструктор")
    def test_open_constructor(self, driver):
        constructor_page = ConstructorPage(driver)

        constructor_page.open()
        constructor_page.click_order_feed()
        constructor_page.click_constructor()

        assert constructor_page.is_bun_displayed()

    @allure.title("Открытие деталей ингредиента")
    def test_open_ingredient_details(self, driver):
        constructor_page = ConstructorPage(driver)

        constructor_page.open()
        constructor_page.click_ingredient()

        assert constructor_page.is_ingredient_modal_displayed()

    @allure.title("Закрытие деталей ингредиента")
    def test_close_ingredient_details(self, driver):
        constructor_page = ConstructorPage(driver)

        constructor_page.open()
        constructor_page.click_ingredient()
        constructor_page.close_ingredient_modal()

        assert not constructor_page.is_ingredient_modal_displayed()

    @allure.title("Каунтер булки увеличивается после добавления в заказ")
    def test_bun_counter_increases(self, driver):
        constructor_page = ConstructorPage(driver)

        constructor_page.open()
        initial_counter = constructor_page.get_bun_counter()
        constructor_page.drag_bun_to_basket()

        assert constructor_page.wait_for_bun_counter_increase(
            initial_counter
        )

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_create_order(self, driver, test_user):
        login_page = LoginPage(driver)
        constructor_page = ConstructorPage(driver)

        login_page.open()
        login_page.login(
            test_user["email"],
            test_user["password"]
        )

        constructor_page.drag_bun_to_basket()
        constructor_page.click_order()

        order_number = constructor_page.get_order_number()

        assert order_number.isdigit()
