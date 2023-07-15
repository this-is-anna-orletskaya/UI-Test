import pytest 




def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")


@pytest.fixture(scope="function")
def setup(request):
    from selenium import webdriver

    print("Начало теста")

    browser = request.config.getoption('browser')

    if browser == "firefox":
        driver = webdriver.Firefox(executable_path="E:\Resourse\GeckoDriver\\geckodriver.exe")
    
    elif browser == "chrome":
        driver = webdriver.Chrome(executable_path="E:\Resourse\ChromeDriver\\chromedriver.exe")

    driver.maximize_window()

    request.cls.driver = driver

    yield

    driver.close()
    if driver != None:
        driver.quit()
    
    print("Конец теста")

