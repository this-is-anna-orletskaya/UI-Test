import sys
sys.path.append('./utils/')
sys.path.append('./testdata/')
from main_page import MainPage
from locators import RegisterPageLocators
from base_methods import BaseMethods




"""Страница регистрации на сайте"""

class RegisterPage(BaseMethods):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    url = "https://try.vikunja.io/register"

    def input_username(self, username):
        self.get_element_to_be_clickable_by_xpath(RegisterPageLocators.username_field_locator).send_keys(username)

    def input_email(self, email):
        self.get_element_to_be_clickable_by_xpath(RegisterPageLocators.email_field_locator).send_keys(email)
    
    def input_password(self, password):
        self.get_element_to_be_clickable_by_xpath(RegisterPageLocators.password_field_locator).send_keys(password)
    
    def click_create_account(self):
        self.get_element_to_be_clickable_by_xpath(RegisterPageLocators.create_account_button_locator).click()

    def click_go_log_in(self):
        self.get_element_to_be_clickable_by_xpath(RegisterPageLocators.go_log_in_locator).click()
    
    def cheking_message(self):
        return self.get_element_to_be_clickable_by_xpath(RegisterPageLocators.check_message_locator)
    
    def register(self, username, email, password):
        self.input_username(username)
        self.input_email(email)
        self.input_password(password)
        self.click_create_account()
        