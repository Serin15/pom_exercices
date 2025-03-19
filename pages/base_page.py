from browser import Browser


class BasePage(Browser):
    def __init__(self, webdriver):
        super().__init__()
        self.driver = webdriver

        def find(self, locator):
            return self.driver.find_element(*locator)

        def find_all(self, locator):
            return self.driver.find_elements(*locator)

        def type(self, locator, text):
             self.find(locator).send_keys(text)

        def click(self, locator):
            self.find(locator).click()

        def verify_current_url(self, expected_url):
            return self.driver.current_url == expected_url

        def is_element_absent(self, locator):
            return len(self.find_all(locator)) == 0