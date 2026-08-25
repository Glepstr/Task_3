from selenium.webdriver.common.by import By


class ConstructorLocators:
    CONSTRUCTOR_LINK = (
        By.XPATH,
        "//a[@href='/']"
    )

    ORDER_FEED_LINK = (
        By.XPATH,
        "//a[@href='/feed']"
    )

    BUN = (
        By.XPATH,
        "//a[@href='/ingredient/691577430cc94f001a65b859']"
    )

    BUN_COUNTER = (
        By.XPATH,
        "//a[@href='/ingredient/691577430cc94f001a65b859']"
        "//p[contains(@class, 'counter_counter__num')]"
    )

    INGREDIENT_MODAL_TITLE = (
        By.XPATH,
        "//h2[normalize-space()='Детали ингредиента']"
    )

    BASKET = (
        By.CSS_SELECTOR,
        ".BurgerConstructor_basket__list__l9dp_"
    )

    ORDER_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Оформить заказ']"
    )

    CLOSE_INGREDIENT_MODAL = (
        By.XPATH,
        "//h2[normalize-space()='Детали ингредиента']"
        "/ancestor::section[1]"
        "//button[@type='button']"
    )

    ORDER_NUMBER = (
        By.XPATH,
        "//h2[contains(@class, 'Modal_modal__title_shadow')]"
    )

    ORDER_MODAL_CLOSE = (
        By.CSS_SELECTOR,
        "button.Modal_modal__close__TnseK"
    )
    