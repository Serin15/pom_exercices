from selenium import webdriver


class Browser:


    def __init__(self):
        self.driver = None

    def get_driver(self):
        if self.driver is None:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(3)
        return self.driver

    def close_browser(self):
        if self.driver:
            self.driver.quit()
            self.driver = None