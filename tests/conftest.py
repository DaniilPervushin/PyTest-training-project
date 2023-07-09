import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    b = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    b.maximize_window()
    b.implicitly_wait(10)

    yield b

    b.quit()

