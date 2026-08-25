from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from utils.constants import ORDER_FEED_URL


class OrderFeedPage(BasePage):

    URL = ORDER_FEED_URL

    def open(self):
        super().open(self.URL)

    def click_first_order(self):
        self.click(OrderFeedLocators.FIRST_ORDER)

    def is_order_modal_visible(self):
        return self.is_element_visible(
            OrderFeedLocators.ORDER_MODAL
        )

    def get_modal_order_number(self):
        return self.get_text(
            OrderFeedLocators.MODAL_ORDER_NUMBER
        )

    def get_order_numbers(self):
        self.wait_for_orders()

        return [
            element.text
            for element in self.find_elements(
                OrderFeedLocators.ORDER_NUMBERS
            )
        ]

    def wait_for_order(self, order_number):
        expected_order = f"#{order_number.zfill(6)}"

        self.wait.until(
            lambda driver: expected_order in [
                element.text
                for element in self.find_elements(
                    OrderFeedLocators.ORDER_NUMBERS
                )
            ]
        )
        return True

    def wait_for_orders(self):
        self.wait.until(
            lambda driver: self.find_elements(
                OrderFeedLocators.FIRST_ORDER
            )
        )

    def get_total_orders_count(self):
        return int(
            self.get_text(
                OrderFeedLocators.TOTAL_ORDERS_COUNTER
            )
        )

    def get_today_orders_count(self):
        return int(
            self.get_text(
                OrderFeedLocators.TODAY_ORDERS_COUNTER
            )
        )

    def wait_for_total_orders_count_increase(self, initial_count):
        self.wait.until(
            lambda driver:
            self.get_total_orders_count() > initial_count
        )
        return True

    def wait_for_today_orders_count_increase(self, initial_count):
        self.wait.until(
            lambda driver:
            self.get_today_orders_count() > initial_count
        )
        return True

    def wait_for_order_in_work(self, order_number):
        formatted_number = order_number.zfill(6)

        self.wait.until(
            lambda driver: formatted_number in [
                element.text
                for element in self.find_elements(
                    OrderFeedLocators.WORKING_ORDER_NUMBERS
                )
            ]
        )
        return True
