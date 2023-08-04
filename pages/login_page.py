import sys
sys.path.append('./utils/')
sys.path.append('./testdata/')
from locators import LoginPageLocators
from base_methods import BaseMethods
from logger import Logger




"""Страница авторизации на сайте"""

class LoginPage(BaseMethods):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = "https://try.vikunja.io/login"

    def input_login(self, login):
        self.get_element_to_be_clickable(LoginPageLocators.username_field_locator).send_keys(login)
    
    def input_password(self, password):
        self.get_element_to_be_clickable(LoginPageLocators.password_field_locator).send_keys(password)
    
    def click_remember_me(self):
        self.get_element_to_be_clickable(LoginPageLocators.remember_me_chekbox_locator).click()

    def click_log_in(self):
        self.get_element_to_be_clickable(LoginPageLocators.log_in_button_locator).click()
    
    def check_title(self):
        return self.get_element_is_visible(LoginPageLocators.check_title_locator)

    def check_danger_message(self):
        return self.get_element_is_visible(LoginPageLocators.check_danger_message_locator)
    
    def check_danger_message_not_appear(self):
        return self.get_element_is_not_visible(LoginPageLocators.check_danger_message_locator)
    

    """Основные тестовые методы"""

    def log_in(self, request, login, password):
        self.input_login(login)
        Logger.add_to_log(request).debug("Input login")
        self.input_password(password)
        Logger.add_to_log(request).debug("Input password")
        self.click_remember_me()
        Logger.add_to_log(request).debug("Click checkbox")
        self.click_log_in()
        Logger.add_to_log(request).debug("Click log in")
    
