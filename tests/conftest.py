import pathlib
import pytest 



environment_properties = True

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


def create_allure_environment(driver, allure_dir, browser):

    browser_version = driver.capabilities['browserVersion']

    with open(f"{allure_dir}{pathlib.os.sep}environments.properties", "w") as file:
        file.write(f"Browser={browser.capitalize()}")
        file.write(f"\nBrowser.Version={browser_version}")


@pytest.fixture(scope="function")
def setup(request):
    from selenium import webdriver

    print("Начало теста")

    browser = request.config.getoption('browser')
    allure_dir = request.config.option.allure_report_dir


    if browser == "firefox":
        driver = webdriver.Firefox()
    
    elif browser == "chrome":
        driver = webdriver.Chrome()

    driver.maximize_window()

    request.cls.driver = driver

    global environment_properties
    if environment_properties is True:
        create_allure_environment(driver, allure_dir, browser)
        environment_properties = False

    yield

    driver.close()
    if driver != None:
        driver.quit()
    
    print("Конец теста")


