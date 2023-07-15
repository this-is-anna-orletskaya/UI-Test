from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import datetime



class BaseMethods:
    
    url = "https://try.vikunja.io/"
    
    def __init__(self, driver):
        self.driver = driver
    
    def load(self):
        self.driver.get(self.url)

    def get_element_to_be_clickable_by_xpath(self, locator: str):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, locator)))
    
    def save_screenshot(self):
        now_date =  datetime.datetime.utcnow().strftime("%d.%m.%Y.%H.%M.%S.")
        name_screen = now_date + ".png"
        self.driver.save_screenshot("./screenshots//" + name_screen)
