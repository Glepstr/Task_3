from selenium.webdriver.common.by import By


class LoginLocators:
    EMAIL_INPUT = (By.NAME, "name")
    PASSWORD_INPUT = (By.NAME, "Пароль")

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Войти']"
    )

    REGISTER_LINK = (
        By.XPATH,
        "//a[normalize-space()='Зарегистрироваться']"
    )

    FORGOT_PASSWORD_LINK = (
        By.XPATH,
        "//a[normalize-space()='Восстановить пароль']"
    )

    PASSWORD_VISIBILITY_BUTTON = (
        By.CSS_SELECTOR,
        ".input_type_password .input__icon-action"
    )

    OVERLAY = (
        By.CSS_SELECTOR,
        ".Modal_modal_overlay__x2ZCr"
    )

    ACCOUNT_LINK = (
        By.XPATH,
        "//a[@href='/account']"
    )