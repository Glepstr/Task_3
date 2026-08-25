from selenium.webdriver.common.by import By


class OrderFeedLocators:

    FIRST_ORDER = (
        By.CSS_SELECTOR,
        "a[href^='/feed/']"
    )

    ORDER_MODAL = (
        By.CSS_SELECTOR,
        "div.Modal_orderBox__1xWdi"
    )

    MODAL_ORDER_NUMBER = (
        By.CSS_SELECTOR,
        "div.Modal_orderBox__1xWdi > p"
    )

    ORDER_NUMBERS = (
        By.CSS_SELECTOR,
        "p.text_type_digits-default"
    )

    TOTAL_ORDERS_COUNTER = (
        By.XPATH,
        "//p[normalize-space()='Выполнено за все время:']"
        "/following-sibling::p"
    )

    TODAY_ORDERS_COUNTER = (
        By.XPATH,
        "//p[normalize-space()='Выполнено за сегодня:']"
        "/following-sibling::p"
    )

    WORKING_ORDER_NUMBERS = (
        By.XPATH,
        "//p[normalize-space()='В работе:']"
        "/following-sibling::ul/li"
    )