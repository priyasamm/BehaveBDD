from selenium import webdriver

from utilities import ConfigReader


def before_scenario(context, driver):
    browser = ConfigReader.read_configuration("basic info", "browser")
    if browser.__eq__("chrome"):
        context.driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        context.driver = webdriver.Firefox()
    elif browser.__eq__("safari"):
        context.driver = webdriver.Safari()
    elif browser.__eq__("ie"):
        context.driver = webdriver.Ie()
    elif browser.__eq__("edge"):
        context.driver = webdriver.Edge()
    else:
        print("Default browser")
        context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configuration("basic info", "url"))


def after_scenario(context, driver):
    context.driver.quit()
