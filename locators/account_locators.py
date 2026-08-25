from selenium.webdriver.common.by import By


class AccountLocators:
    ORDER_HISTORY_LINK = (
        By.XPATH,
        "//a[@href='/account/order-history']"
    )

    ACTIVE_ORDER_HISTORY_LINK = (
        By.XPATH,
        "//a[@href='/account/order-history' and @aria-current='page']"
    )

    LOGOUT_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Выход']"
    )

    ORDER_NUMBERS = (
        By.CSS_SELECTOR,
        "li.OrderHistory_listItem__2x95r p.text_type_digits-default"
    )