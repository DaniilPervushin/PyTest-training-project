def test_duck_duck_go_search_page_open(browser):
    browser.get("https://duckduckgo.com/")
    assert 'DuckDuckGo' in browser.title

