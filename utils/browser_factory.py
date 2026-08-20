from selenium import webdriver


class BrowserFactory:

    @staticmethod
    def create_driver(browser):
        if browser.lower() == "chrome":
            return webdriver.Chrome()

        if browser.lower() == "firefox":
            return webdriver.Firefox()

        raise ValueError(f"Unsupported browser: {browser}")