import allure

from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage


class TestOrderFeed:

    @allure.title("Открытие деталей заказа в ленте")
    def test_open_order_details(self, driver):
        order_feed_page = OrderFeedPage(driver)

        order_feed_page.open()
        order_feed_page.wait_for_orders()
        order_feed_page.click_first_order()

        assert order_feed_page.is_order_modal_visible()

    @allure.title("Созданный заказ отображается в ленте заказов")
    def test_created_order_appears_in_feed(self, driver, test_user):
        login_page = LoginPage(driver)
        constructor_page = ConstructorPage(driver)
        order_feed_page = OrderFeedPage(driver)

        login_page.open()
        login_page.login(
            test_user["email"],
            test_user["password"]
        )

        constructor_page.drag_bun_to_basket()
        constructor_page.click_order()

        order_number = constructor_page.get_order_number()

        order_feed_page.open()

        assert order_feed_page.wait_for_order(order_number)

    @allure.title("Номер заказа отображается в деталях заказа")
    def test_order_number_in_details(self, driver):
        order_feed_page = OrderFeedPage(driver)

        order_feed_page.open()
        order_feed_page.wait_for_orders()
        order_feed_page.click_first_order()

        order_number = order_feed_page.get_modal_order_number()

        assert order_number.startswith("#")

    @allure.title("Счётчик выполненных заказов за всё время увеличивается")
    def test_total_orders_counter_increases(self, driver, test_user):
        login_page = LoginPage(driver)
        constructor_page = ConstructorPage(driver)
        order_feed_page = OrderFeedPage(driver)

        order_feed_page.open()
        initial_count = order_feed_page.get_total_orders_count()

        login_page.open()
        login_page.login(
            test_user["email"],
            test_user["password"]
        )

        constructor_page.drag_bun_to_basket()
        constructor_page.click_order()
        constructor_page.get_order_number()

        order_feed_page.open()

        assert order_feed_page.wait_for_total_orders_count_increase(
            initial_count
        )

    @allure.title("Счётчик выполненных заказов за сегодня увеличивается")
    def test_today_orders_counter_increases(self, driver, test_user):
        login_page = LoginPage(driver)
        constructor_page = ConstructorPage(driver)
        order_feed_page = OrderFeedPage(driver)

        order_feed_page.open()
        initial_count = order_feed_page.get_today_orders_count()

        login_page.open()
        login_page.login(
            test_user["email"],
            test_user["password"]
        )

        constructor_page.drag_bun_to_basket()
        constructor_page.click_order()
        constructor_page.get_order_number()

        order_feed_page.open()

        assert order_feed_page.wait_for_today_orders_count_increase(
            initial_count
        )

    @allure.title("Созданный заказ появляется в разделе «В работе»")
    def test_created_order_appears_in_work(self, driver, test_user):
        login_page = LoginPage(driver)
        constructor_page = ConstructorPage(driver)
        order_feed_page = OrderFeedPage(driver)

        login_page.open()
        login_page.login(
            test_user["email"],
            test_user["password"]
        )

        constructor_page.drag_bun_to_basket()
        constructor_page.click_order()

        order_number = constructor_page.get_order_number()

        order_feed_page.open()

        assert order_feed_page.wait_for_order_in_work(order_number)
