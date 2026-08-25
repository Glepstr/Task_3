from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    EMAIL_INPUT = (
        By.NAME,
        "name"
    )

    RESTORE_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Восстановить']"
    )

    PASSWORD_CONTAINER = (
        By.XPATH,
        "//input[@name='Введите новый пароль']/parent::div"
    )

    PASSWORD_INPUT = (
        By.NAME,
        "Введите новый пароль"
    )

    PASSWORD_TOGGLE = (
        By.CSS_SELECTOR,
        ".input_type_password .input__icon-action"
    )

    CODE_INPUT = (
        By.XPATH,
        "//input[@name='name' and @type='text']"
    )

    SAVE_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Сохранить']"
    )

    LOGIN_LINK = (
        By.XPATH,
        "//a[normalize-space()='Войти']"
    )