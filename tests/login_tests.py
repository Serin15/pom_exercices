import unittest

from pages.login_page import LoginPage


class LoginTests(unittest.TestCase):

    def setUp(self):
        self.login_page = LoginPage()
        self.login_page.open()

    def tearDown(self):
        self.login_page.close_browser()


    def test_successful_login(self):
        self.login_page.login("standard_user", "secret_sauce")
        assert self.login_page.verify_current_url("https://www.saucedemo.com/inventory.html")