import sys
sys.path.append('./utils/')
sys.path.append('./testdata/')
from locators import LoginPageLocators
from base_methods import BaseMethods




"""Страница авторизации на сайте"""

class LoginPage(BaseMethods):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = "https://try.vikunja.io/login"

    def input_login(self, login):
        self.get_element_to_be_clickable_by_xpath(LoginPageLocators.username_field_locator).send_keys(login)
    
    def input_password(self, password):
        self.get_element_to_be_clickable_by_xpath(LoginPageLocators.password_field_locator).send_keys(password)
    
    def click_remember_me(self):
        self.get_element_to_be_clickable_by_xpath(LoginPageLocators.remember_me_chekbox_locator).click()

    def click_log_in(self):
        self.get_element_to_be_clickable_by_xpath(LoginPageLocators.log_in_button_locator).click()
    
    def check_title(self):
        return self.get_element_to_be_clickable_by_xpath(LoginPageLocators.check_title_locator)

    def check_danger_message(self):
        return self.get_element_to_be_clickable_by_xpath(LoginPageLocators.check_danger_message_locator)

    
    """Основные тестовые методы"""

    def log_in(self, login, password):
        self.input_login(login)
        self.input_password(password)
        self.click_remember_me()
        self.click_log_in()