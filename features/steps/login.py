import time
from datetime import *

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from features.Pages.AccountPage import AccountPage
from features.Pages.LoginPage import LoginPage
from features.Pages.HomePage import HomePage


@given(u'I navigate to login page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_myaccount()
    context.home_page.select_login_option()


@when(u'I enter valid {email} and valid {password} into the fields')
def step_impl(context,email,password):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address(email)
    context.login_page.enter_password(password)


@when(u'I click on Login button')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.click_on_login_button()


@then(u'I should get logged in')
def step_impl(context):
    context.account_page = AccountPage(context.driver)
    assert context.account_page.display_status_of_edit_your_information_option()


@when(u'I enter invalid email and valid password into the fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    time_stamp = datetime.now().strftime("%y %m %d %h %M %S")
    invalid_email = "priyasam" + time_stamp + "@gmail.com"
    context.login_page.enter_email_address(invalid_email)
    context.login_page.enter_password("12345")


@then(u'I should get proper warning message')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    expected_text = "Warning: No match for E-Mail Address and/or Password."
    assert context.login_page.verify_warning_message(expected_text)


@when(u'I enter valid email and invalid password into the fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address("priyasam1111@gmail.com")
    context.login_page.enter_password("123456")


@when(u'I enter invalid email and invalid password into the fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    time_stamp = datetime.now().strftime("%y_%m_%d_%h_%M_%S")
    invalid_email = "priyasam" + time_stamp + "@gmail.com"
    context.login_page.enter_email_address(invalid_email)
    context.login_page.enter_password(time_stamp)


@when(u'I enter without email and password into the fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address("")
    context.login_page.enter_password("")
