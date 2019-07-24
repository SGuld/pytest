import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                 help="Choose browser: chrome or firefox")
    parser.addoption('--language_name', action='store', default="es",
                 help="Choose language: es or fr")

@pytest.fixture(scope="function")
def language(request):
    language_name = request.config.getoption("language_name")
    if language_name == "es":
        language = "http://selenium1py.pythonanywhere.com/es/catalogue/coders-at-work_207/"
    elif language_name == "fr":
        language = "http://selenium1py.pythonanywhere.com/fr/catalogue/coders-at-work_207/"
    yield language
    
    
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        print("Browser {} still is not implemented".format(browser_name))
    yield browser
    print("\nquit browser..")
    browser.quit()
    
