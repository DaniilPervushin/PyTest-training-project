import pytest
from pages.search_page import DuckDuckGoSearchPage
from pages.result_page import DuckDuckGoResultPage



@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_search_using_keys(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    search_page.duckduckgo_home_page_load()
    search_page.search_using_keys(phrase)
    assert len([t for t in result_page.f_result_link_titles() if phrase.lower() in t.lower()]) > 0
    assert (phrase + ' at DuckDuckGo') in result_page.title()


@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_search_using_search_button(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    search_page.duckduckgo_home_page_load()
    search_page.search_using_button(phrase)
    assert len([t for t in result_page.f_result_link_titles() if phrase.lower() in t.lower()]) > 0
