from datetime import datetime

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from features.Pages.RegisterPage import RegisterPage


@given(u'I navigate to register page')
def step_impl(context):
    context.register_page=RegisterPage(context.driver)
    context.register_page.click_on_myaccount_drp()
    context.register_page.click_on_register_option()


@when(u'I enter mandatory fields')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_firstname("Priya")
    context.register_page.enter_lastname("Sam")
    time_stamp = datetime.now().strftime("%y_%m_%d_%h_%M_%S")
    email = "priyasam" + time_stamp + "@gmail.com"
    print(email)
    context.register_page.enter_emailid(email)
    context.register_page.enter_telephone("1234567890")
    context.register_page.enter_password("12345")
    context.register_page.enter_confirm("12345")


@when(u'I select privacy policy option')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.click_on_agree_option()


@when(u'I click on continue button')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.click_on_continue_button()


@then(u'Account should get created')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    expected_text = "Your Account Has Been Created!"
    assert context.register_page.check_accountcreation_text(expected_text)


@when(u'I enter details into all fields')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_firstname("Priya")
    context.register_page.enter_lastname("Sam")
    time_stamp = datetime.now().strftime("%y_%m_%d_%h_%M_%S")
    email = "priyasam" + time_stamp + "@gmail.com"
    print(email)
    context.register_page.enter_emailid(email)
    context.register_page.enter_telephone("1234567890")
    context.register_page.enter_password("12345")
    context.register_page.enter_confirm("12345")
    context.register_page.select_newletter_option()


@when(u'I enter existing account email into the email field')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_firstname("Priya")
    context.register_page.enter_lastname("Sam")
    context.register_page.enter_emailid("priyasam1111@gmail.com")
    context.register_page.enter_telephone("1234567890")
    context.register_page.enter_password("12345")
    context.register_page.enter_confirm("12345")
    context.register_page.select_newletter_option()

@then(u'Proper warning message informing about duplicate account should be displayed')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    expected_text = "Warning: E-Mail Address is already registered!"
    assert context.register_page.check_warning_text(expected_text)


@when(u'I dont enter anything into the fields')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_firstname("")
    context.register_page.enter_lastname("")
    context.register_page.enter_emailid("")
    context.register_page.enter_telephone("")
    context.register_page.enter_password("")
    context.register_page.enter_confirm("")


@then(u'Proper warning message for every mandatory fields should be displayed')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    expected_text = "Warning: You must agree to the Privacy Policy!"
    expected_firstname_warning = "First Name must be between 1 and 32 characters!"
    expected_lastname_warning = "Last Name must be between 1 and 32 characters!"
    expected_email_warning = "E-Mail Address does not appear to be valid!"
    expected_telephone_warning = "Telephone must be between 3 and 32 characters!"
    expected_password_warning = "Password must be between 4 and 20 characters!"
    assert context.register_page.agree_warning_text(expected_text)
    assert context.register_page.firstname_warning_text(expected_firstname_warning)
    assert context.register_page.lastname_warning_text(expected_lastname_warning)
    assert context.register_page.email_warning_text(expected_email_warning)
    assert context.register_page.telephone_warning_text(expected_telephone_warning)
    assert context.register_page.password_warning_text(expected_password_warning)

