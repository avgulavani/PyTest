import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
@pytest.fixture(params=["chrome","firefox"],scope='class')
def init_driver(request):
    if request.param=='chrome':
        web_driver=webdriver.Chrome()
    if request.param=='firefox':
        web_driver=webdriver.Firefox()
    request.cls.driver=web_driver
    yield
    web_driver.close()
@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class Test_E2E(BaseTest):
    def test_open_page(self):
        self.driver.get('http://www.google.com')