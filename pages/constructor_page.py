from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from locators.constructor_locators import ConstructorLocators
from locators.base_locators import BaseLocators


class ConstructorPage(BasePage):

    URL = "https://qa-stellarburgers.education-services.ru/"

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
        elements = self.driver.find_elements(
            *ConstructorLocators.INGREDIENT_MODAL_TITLE
        )

        return bool(elements) and elements[0].is_displayed()

    def get_bun_counter(self):
        return int(
            self.find_element(
                ConstructorLocators.BUN_COUNTER
            ).text
        )

    def drag_bun_to_basket(self):
        self.wait_for_modals_to_disappear()

        bun = self.find_element(ConstructorLocators.BUN)
        basket = self.find_element(ConstructorLocators.BASKET)

        if self.driver.name == "firefox":
            self.driver.execute_script(
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
                """, # Способа лучше не нашел. Сидел с нейронкой, пробовал много чего, ничего не помогло кроме этой сложной конструкции.
                bun,
                basket
            )

            return

        ActionChains(self.driver).drag_and_drop(
            bun,
            basket
        ).perform()
    
    def click_order(self):
        self.wait_for_modals_to_disappear()
        self.click(ConstructorLocators.ORDER_BUTTON)

    def wait_for_bun_counter_increase(self, initial_counter):
        self.wait.until(
            lambda driver: int(
                self.find_element(
                    ConstructorLocators.BUN_COUNTER
                ).text
            ) > initial_counter
        )

    def get_order_number(self):
        return self.wait.until(
            lambda driver: (
                number
                if number != "9999"
                else False
            )
            if (number := driver.find_element(
                *ConstructorLocators.ORDER_NUMBER
            ).text)
            else False
        )

    def is_order_modal_displayed(self):
        return self.find_element(
            ConstructorLocators.ORDER_NUMBER
        ).is_displayed()

    def close_order_modal(self):
        self.click(ConstructorLocators.ORDER_MODAL_CLOSE)

        self.wait.until(
            lambda driver: all(
                not overlay.is_displayed()
                for overlay in driver.find_elements(
                    *BaseLocators.MODAL_OVERLAYS
                )
            )
        )