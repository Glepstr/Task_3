from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):

    URL = "https://qa-stellarburgers.education-services.ru/feed"

    def open(self):
        super().open(self.URL)

    def click_first_order(self):
        self.click(OrderFeedLocators.FIRST_ORDER)

    def is_order_modal_visible(self):
        return self.is_element_visible(
            OrderFeedLocators.ORDER_MODAL
        )

    def get_modal_order_number(self):
        return self.find_element(
            OrderFeedLocators.MODAL_ORDER_NUMBER
        ).text

    def get_order_numbers(self):
        self.wait.until(
            lambda driver: len(
                driver.find_elements(
                    *OrderFeedLocators.ORDER_NUMBERS
                )
            ) > 0
        )

        return [
            element.text
            for element in self.driver.find_elements(
                *OrderFeedLocators.ORDER_NUMBERS
            )
        ]

    def wait_for_order(self, order_number):
        expected_order = f"#{order_number.zfill(6)}"

        self.wait.until(
            lambda driver: expected_order in [
                element.text
                for element in driver.find_elements(
                    *OrderFeedLocators.ORDER_NUMBERS
                )
            ]
        )

    def wait_for_orders(self):
        self.wait.until(
            lambda driver: driver.find_elements(
                *OrderFeedLocators.FIRST_ORDER
            )
        )

    def get_total_orders_count(self):
        return int(
            self.find_element(
                OrderFeedLocators.TOTAL_ORDERS_COUNTER
            ).text
        )

    def get_today_orders_count(self):
        return int(
            self.find_element(
                OrderFeedLocators.TODAY_ORDERS_COUNTER
            ).text
        )

    def wait_for_order_in_work(self, order_number):
        formatted_number = order_number.zfill(6)

        self.wait.until(
            lambda driver: formatted_number in [
                element.text
                for element in driver.find_elements(
                    *OrderFeedLocators.WORKING_ORDER_NUMBERS
                )
            ]
        )