from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from features.Pages.HomePage import HomePage
from features.Pages.SearchPage import SearchPage


@given(u'I got navigated to the home page')
def step_impl(context):
    expected_text = "Your Store"
    context.search_page = SearchPage(context.driver)
    assert context.search_page.verify_title_message(expected_text)


@when(u'I enter valid product in search box field')
def step_impl(context):
    context.search_page = SearchPage(context.driver)
    context.search_page.enter_searchtext("HP")

@when(u'I click on search button')
def step_impl(context):
    context.search_page = SearchPage(context.driver)
    context.search_page.click_search_button()


@then(u'Valid product gets displayed in the search results')
def step_impl(context):
    context.search_page = SearchPage(context.driver)
    assert context.search_page.check_if_displayed()


@when(u'I enter invalid product in search box field')
def step_impl(context):
    context.search_page = SearchPage(context.driver)
    context.search_page.enter_searchtext("Honda")


@then(u'Proper error message displayed in the search results')
def step_impl(context):
    context.search_page = SearchPage(context.driver)
    expected_text = "There is no product that matches the search criteria."
    assert context.search_page.verify_warning_message(expected_text)


@when(u'I dont enter anything in search box field')
def step_impl(context):
    context.search_page = SearchPage(context.driver)
    context.search_page.enter_searchtext("")
