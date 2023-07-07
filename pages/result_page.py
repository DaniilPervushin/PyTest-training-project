from selenium.webdriver.common.by import By
class DuckDuckGoResultPage:
    results = (By.CSS_SELECTOR, 'a[data-testid="result-title-a"]')


    def __init__(self, browser):
        self.browser = browser


    def f_result_link_titles(self):
        links = self.browser.find_elements(*self.results)
        titles = [link.text for link in links]
        return titles


    def title(self):
        return self.browser.title


