from features.Pages.BasePage import BasePage


class RegisterPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    drp_myaccount_link_text="My Account"
    option_register_link_text="Register"
    input_firstname_id="input-firstname"
    input_lastname_id="input-lastname"
    input_email_id="input-email"
    input_telephone_id="input-telephone"
    input_password_id="input-password"
    input_confirm_id="input-confirm"
    checkbox_agree_name="agree"
    button_continue_xpath="//*[@value='Continue']"
    check_accountcreate_xpath="//*[@id='content']/h1"
    checkbox_newsletter_xpath="//*[@name='newsletter'][@value='1']"
    duplicate_text_xpath="//*[@id='account-register']//div[1]"
    agree_warning_xpath="//*[@id='account-register']//div[1]"
    firstname_warning_xpath="//*[@name='firstname']/following-sibling::div"
    lastname_warning_xpath="//*[@name='lastname']/following-sibling::div"
    email_warning_xpath="//*[@name='email']/following-sibling::div"
    telephone_warning_xpath="//*[@name='telephone']/following-sibling::div"
    password_warning_xpath="//*[@name='password']/following-sibling::div"
    def click_on_myaccount_drp(self):
        self.click_on_element("drp_myaccount_link_text",self.drp_myaccount_link_text)

    def click_on_register_option(self):
        self.click_on_element("option_register_link_text",self.option_register_link_text)

    def enter_firstname(self, firstname_text):
        self.type_into_element("input_firstname_id", self.input_firstname_id, firstname_text)

    def enter_lastname(self, lastname_text):
        self.type_into_element("input_lastname_id", self.input_lastname_id, lastname_text)

    def enter_emailid(self, email_text):
        self.type_into_element("input_email_id", self.input_email_id, email_text)

    def enter_telephone(self, telephone_text):
        self.type_into_element("input_telephone_id", self.input_telephone_id, telephone_text)

    def enter_password(self, password_text):
        self.type_into_element("input_password_id", self.input_password_id, password_text)

    def enter_confirm(self, confirm_text):
        self.type_into_element("input_confirm_id", self.input_confirm_id, confirm_text)

    def click_on_agree_option(self):
        self.click_on_element("checkbox_agree_name",self.checkbox_agree_name)

    def click_on_continue_button(self):
        self.click_on_element("button_continue_xpath",self.button_continue_xpath)

    def check_accountcreation_text(self,expected_text):
        assertvalue = self.verify_text("check_accountcreate_xpath", self.check_accountcreate_xpath, expected_text)
        return assertvalue

    def select_newletter_option(self):
        self.click_on_element("checkbox_newsletter_xpath",self.checkbox_newsletter_xpath)

    def check_warning_text(self,expected_text):
        assertvalue = self.verify_text("duplicate_text_xpath", self.duplicate_text_xpath, expected_text)
        return assertvalue

    def agree_warning_text(self,expected_text):
        assertvalue = self.verify_text("agree_warning_xpath", self.agree_warning_xpath, expected_text)
        return assertvalue
    def firstname_warning_text(self,expected_text):
        assertvalue = self.verify_text("firstname_warning_xpath", self.firstname_warning_xpath, expected_text)
        return assertvalue
    def lastname_warning_text(self,expected_text):
        assertvalue = self.verify_text("lastname_warning_xpath", self.lastname_warning_xpath, expected_text)
        return assertvalue
    def email_warning_text(self,expected_text):
        assertvalue = self.verify_text("email_warning_xpath", self.email_warning_xpath, expected_text)
        return assertvalue
    def telephone_warning_text(self,expected_text):
        assertvalue = self.verify_text("telephone_warning_xpath", self.telephone_warning_xpath, expected_text)
        return assertvalue
    def password_warning_text(self,expected_text):
        assertvalue = self.verify_text("password_warning_xpath", self.password_warning_xpath, expected_text)
        return assertvalue