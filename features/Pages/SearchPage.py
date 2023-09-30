from features.Pages.BasePage import BasePage


class SearchPage(BasePage):
    def  __init__(self,driver):
        super().__init__(driver)

    searchbox_name="search"
    warning_message_xpath="//*[@id='button-search']/following-sibling::p"
    invalid_search_link_text = "HP LP3065"
    search_button_xpath="//*[@id='search']//button"
    def verify_title_message(self, expected_text):
        assertvalue = self.verify_page_title(expected_text)
        return assertvalue

    def enter_searchtext(self,search_text):
        self.type_into_element("searchbox_name", self.searchbox_name,search_text)

    def verify_warning_message(self, expected_text):
        assertvalue = self.verify_text("warning_message_xpath", self.warning_message_xpath, expected_text)
        return assertvalue

    def check_if_displayed(self):
        assertvalue=self.verify_status_of_element("invalid_search_link_text",self.invalid_search_link_text)
        return assertvalue

    def click_search_button(self):
        self.click_on_element("search_button_xpath", self.search_button_xpath)