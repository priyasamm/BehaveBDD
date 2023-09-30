from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def common_find_element(self, locator_type, locator_value):
        element = None
        print(locator_type + locator_value)
        if locator_type.endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_type.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_type.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_type.endswith("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_type.endswith("_class_name"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_type.endswith("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        return element

    def click_on_element(self,locator_type, locator_value):
        element = self.common_find_element(locator_type, locator_value)
        element.click()

    def verify_page_title(self, expected_title):
        assertvalue = self.assert_validation(self.driver.title.__eq__(expected_title))
        return assertvalue


    def type_into_element(self, locator_type, locator_value, value):
        element = self.common_find_element(locator_type, locator_value)
        element.click()
        element.clear()
        element.send_keys(value)

    def verify_text(self, locator_type, locator_value, expected_value):
        element = self.common_find_element(locator_type, locator_value)
        print("element text is" + element.text + " and expected value is" + expected_value)
        assertvalue=self.assert_validation(element.text.__eq__(expected_value))
        return assertvalue

    def verify_status_of_element(self, locator_type, locator_value):
        element = self.common_find_element(locator_type, locator_value)
        assertvalue = self.assert_validation(element.is_displayed())
        return assertvalue

    def assert_validation(self,condition):
        if (condition):
            print("true")
            return True
        else:
            print("false")
            return False
