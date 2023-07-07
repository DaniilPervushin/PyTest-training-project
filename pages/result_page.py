from selenium.webdriver.common.by import By
class DuckDuckGoResultPage:

    # menu
    all_tab = (By.CSS_SELECTOR, 'a[data-zci-link="web"]')
    images_tab = (By.CSS_SELECTOR, 'a[data-zci-link="images"]')
    videos_tab = (By.CSS_SELECTOR, 'a[data-zci-link="videos"]')
    news_tab = (By.CSS_SELECTOR, 'a[data-zci-link="news"]')
    maps_tab = (By.CSS_SELECTOR, 'a[data-zci-link="maps_expanded"]')

    #all tab
    all_search_results = (By.CSS_SELECTOR, 'a[data-testid="result-title-a"]')

    # images tab
    image_link = (By.CSS_SELECTOR, 'a.tile--img__sub')

    # videos tab
    video_title = (By.XPATH, '//h6[contains(@class, "tile__title") and contains(@class, "tile__title--2")]')

    #news tab
    news_link = (By.CSS_SELECTOR, 'h2.result__title')






    def __init__(self, browser):
        self.browser = browser


    def f_result_link_titles(self):
        links = self.browser.find_elements(*self.all_search_results)
        titles = [link.text for link in links]
        return titles


    def f_result_image_titles(self):
        images = self.browser.find_elements(*self.image_link)
        image_titles = [image_title.text for image_title in images]
        return image_titles


    def f_result_video_titles(self):
        videos = self.browser.find_elements(*self.video_title)
        video_titles = [video_title.text for video_title in videos]
        return video_titles


    def f_result_news_titles(self):
        news = self.browser.find_elements(*self.news_link)
        news_titles = [news_title.text for news_title in news]
        return news_titles


    def title(self):
        return self.browser.title


    def switch_to_videos_tab(self):
        self.browser.find_element(*self.videos_tab).click()


    def switch_to_images_tab(self):
        self.browser.find_element(*self.images_tab).click()


    def switch_to_news_tab(self):
        self.browser.find_element(*self.news_tab).click()


    def switch_to_maps(self):
        self.browser.find_element(*self.maps_tab).click()


