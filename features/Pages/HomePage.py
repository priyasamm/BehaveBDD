from selenium.webdriver.common.by import By

from features.Pages.BasePage import BasePage
from features.Pages.LoginPage import LoginPage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    my_account_option_xpath = "//*[contains(@title,'My Account')]"
    login_option_link_text = "Login"

    def click_on_myaccount(self):
        self.click_on_element("my_account_option_xpath", self.my_account_option_xpath)

    def select_login_option(self):
        self.click_on_element("login_option_link_text", self.login_option_link_text)
        return LoginPage(self.driver)
