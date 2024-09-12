


from selenium import webdriver
from pytest import fixture
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver as FireFox
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.edge.webdriver import WebDriver as Edge


# Hook Function

# pytest_addoption method is used to pass browser and env in terminal

def pytest_addoption(parser):
    parser.addoption("--browser",action = "store", dest = "browser" , default = "Firefox")
    parser.addoption("--env",action = "store", dest = "env", default = "test")


class TestConfiguration:
    url = "http://49.249.28.218:8888/index.php?module=Leads&action=index"

class StageConfiguration:
    url = "https://demowebshop.tricentis.com/login"


@fixture
def _config(request):                  #  a request object, determines the type of browser to use
                                        # based on the request.config.option.browser argument
    if request.config.option.env.upper() == "TEST":
        return TestConfiguration
    elif request.config.option.env.upper() == "STAGE":
        return StageConfiguration
    else:
        return Exception("Invalid Test Environment")

# fixture is callable used to pass data to the test method

@fixture
def _driver(_config,request):

    browser_class = request.config.option.browser.upper()
    if browser_class == "CHROME":
        driver = Chrome()
    elif browser_class == "FIREFOX":
        driver = FireFox()
    elif browser_class == "EDGE":
        driver = Edge()
    else:
        raise Exception("invalid Browser")


    driver.get(_config.url)
    driver.maximize_window()
    yield driver
    driver.close()




