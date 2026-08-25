from pages.base_page import BasePage
from locators.constructor_locators import ConstructorLocators
from utils.constants import CONSTRUCTOR_URL


class ConstructorPage(BasePage):

    URL = CONSTRUCTOR_URL

    def open(self):
        super().open(self.URL)

    def click_constructor(self):
        self.wait_for_modals_to_disappear()
        self.click(ConstructorLocators.CONSTRUCTOR_LINK)

    def click_order_feed(self):
        self.wait_for_modals_to_disappear()
        self.click(ConstructorLocators.ORDER_FEED_LINK)

    def click_ingredient(self):
        self.wait_for_modals_to_disappear()
        self.click(ConstructorLocators.BUN)

    def close_ingredient_modal(self):
        self.click(ConstructorLocators.CLOSE_INGREDIENT_MODAL)
        self.wait_for_element_to_disappear(
            ConstructorLocators.INGREDIENT_MODAL_TITLE
        )

    def is_ingredient_modal_displayed(self):
        return any(
            element.is_displayed()
            for element in self.find_elements(
                ConstructorLocators.INGREDIENT_MODAL_TITLE
            )
        )

    def is_bun_displayed(self):
        return self.is_element_visible(
            ConstructorLocators.BUN
        )

    def get_bun_counter(self):
        return int(
            self.get_text(ConstructorLocators.BUN_COUNTER)
        )

    def drag_bun_to_basket(self):
        self.wait_for_modals_to_disappear()

        bun = self.find_element(ConstructorLocators.BUN)
        basket = self.find_element(ConstructorLocators.BASKET)

        if self.get_browser_name() == "firefox":
            self.execute_script(
                """
                function triggerDragAndDrop(source, target) {
                    const dragStart = new CustomEvent(
                        'dragstart',
                        { bubbles: true, cancelable: true }
                    );

                    const drop = new CustomEvent(
                        'drop',
                        { bubbles: true, cancelable: true }
                    );

                    const dragEnd = new CustomEvent(
                        'dragend',
                        { bubbles: true, cancelable: true }
                    );

                    source.dispatchEvent(dragStart);
                    target.dispatchEvent(drop);
                    source.dispatchEvent(dragEnd);
                }

                triggerDragAndDrop(arguments[0], arguments[1]);
                """,
                bun,
                basket
            )
            return

        self.drag_and_drop(bun, basket)

    def click_order(self):
        self.wait_for_modals_to_disappear()
        self.click(ConstructorLocators.ORDER_BUTTON)

    def wait_for_bun_counter_increase(self, initial_counter):
        self.wait.until(
            lambda driver: self.get_bun_counter() > initial_counter
        )
        return True

    def get_order_number(self):
        return self.wait.until(
            lambda driver: (
                number
                if number != "9999"
                else False
            )
            if (number := self.get_text(
                ConstructorLocators.ORDER_NUMBER
            ))
            else False
        )

    def is_order_modal_displayed(self):
        return self.is_element_visible(
            ConstructorLocators.ORDER_NUMBER
        )

    def close_order_modal(self):
        self.click(ConstructorLocators.ORDER_MODAL_CLOSE)
        self.wait_for_modals_to_disappear()
