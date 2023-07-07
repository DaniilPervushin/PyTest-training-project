import pytest
from pages.search_page import DuckDuckGoSearchPage
from pages.result_page import DuckDuckGoResultPage


phrases =[
    ('snowboard'),
    # ('skate park'),
    # ('horse racing')
]


@pytest.mark.parametrize('phrase', phrases)
def test_search_using_keys(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    search_page.duckduckgo_home_page_load()
    search_page.send_keys_into_search_field(phrase)
    search_page.search_using_keys()
    assert len([t for t in result_page.f_result_link_titles() if phrase.lower() in t.lower()]) > 0
    assert (phrase + ' at DuckDuckGo') in result_page.title()


@pytest.mark.parametrize('phrase', phrases)
def test_search_using_search_button(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    search_page.duckduckgo_home_page_load()
    search_page.send_keys_into_search_field(phrase)
    search_page.search_using_button()
    assert len([t for t in result_page.f_result_link_titles() if phrase.lower() in t.lower()]) > 0


@pytest.mark.parametrize('phrase', phrases)
def test_search_using_suggested_phrases(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    search_page.duckduckgo_home_page_load()
    search_page.send_keys_into_search_field(phrase)
    search_page.select_auto_complete_suggestion()

