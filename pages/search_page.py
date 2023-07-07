from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class DuckDuckGoSearchPage:
    # URL
    url = 'https://www.duckduckgo.com'

    # locators
    search_input_field = (By.ID, 'searchbox_input')
    search_button = (By.CSS_SELECTOR, 'button[aria-label="Search"]')
    auto_complete_suggestions = (By.CSS_SELECTOR, 'li.searchbox_suggestion__csrUQ')

    def __init__(self, browser):
        self.browser = browser

    def f_input_field(self):
        return self.browser.find_element(*self.search_input_field)

    def f_search_button(self):
        return self.browser.find_element(*self.search_button)

    def f_auto_complete_suggestions(self):
        return self.browser.find_elements(*self.auto_complete_suggestions)

    def duckduckgo_home_page_load(self):
        self.browser.get(self.url)

    def search_using_keys(self, phrase):
        self.f_input_field().send_keys(phrase + Keys.RETURN)

    def search_using_button(self, phrase):
        self.f_input_field().send_keys(phrase)
        self.f_search_button().click()

    def auto_complete_content(self):
        suggestions = self.f_auto_complete_suggestions()
        suggestions_text = [suggestion.text for suggestion in suggestions]
        return suggestions_text
