import time

from selenium.webdriver.common.by import By

from features.Pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    input_email_id = "input-email"
    input_password_id = "input-password"
    login_button_xpath = "//*[contains(@value,'Login')]"
    warning_message_xpath = "//*[@id='account-login']/div[1]"

    def enter_email_address(self, email_text):
        self.type_into_element("input_email_id", self.input_email_id, email_text)

    def enter_password(self, password_text):
        self.type_into_element("input_password_id", self.input_password_id, password_text)

    def click_on_login_button(self):
        self.click_on_element("login_button_xpath",self.login_button_xpath)

    def verify_warning_message(self, expected_text):
        assertvalue = self.verify_text("warning_message_xpath",self.warning_message_xpath,expected_text)
        return assertvalue
