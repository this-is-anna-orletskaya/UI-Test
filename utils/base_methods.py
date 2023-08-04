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

    def get_element_to_be_clickable(self, locator: str):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, locator)))
    
    def get_element_is_visible(self, locator: str):
        return WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, locator)))
        
    def save_screenshot(self):
        now_date =  datetime.datetime.utcnow().strftime("%d.%m.%Y.%H.%M.%S.")
        name_screen = now_date + "png"
        self.driver.save_screenshot("./screenshots//" + name_screen)
    
    def get_current_url(self):
        now_url = self.driver.current_url
        print("Текущая URL: " + now_url)
    
    def assert_url(self, expected_url: str):
        now_url = self.driver.current_url
        assert now_url == expected_url
        print("Проверка URL выполнена.")
    
    def assert_text_element(self, word, expected_word: str):
        value_word = word.text 
        assert value_word == expected_word 
        print("Проверка по тексту элемента выполнена.")


    
    
    
    
        
    

