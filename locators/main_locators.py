from selenium.webdriver.common.by import By


class MainLocators:
    PERSONAL_ACCOUNT_LINK = (
        By.XPATH,
        "//a[@href='/account']"
    )