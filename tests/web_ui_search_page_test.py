import pytest
from pages.search_page import DuckDuckGoSearchPage

phrases =[
    ('panda'),
    ('python'),
    ('polar bear'),
    ('snowboard'),
    ('skate park'),
    ('horse racing')
]

@pytest.mark.parametrize('phrase', phrases)
@pytest.mark.searchpage
def test_auto_complete_suggestions_contain_search_phrase(browser, phrase ):
    search_page = DuckDuckGoSearchPage(browser)
    search_page.duckduckgo_home_page_load()
    search_page.f_input_field().send_keys(phrase)
    assert len([t for t in search_page.auto_complete_content() if phrase.lower() in t.lower()]) > 0

