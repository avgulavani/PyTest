import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='module')
def initial_setup():
    global driver;
    print("----------tear_down----------")
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    yield
    print("----------tear_down----------")
    #driver.quit()

def test_site1(initial_setup):
    driver.get("https://www.msn.com/en-in/")

def test_site2():
    driver.get("https://www.indiatoday.in/")


