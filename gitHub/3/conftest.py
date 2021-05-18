import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture()
def driver():
    print("\nstart browser for test..")
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(
        executable_path="/home/user/tms-automated-course/aleksey_burak/3/chromedriver",
        options=chrome_options
    )
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()
