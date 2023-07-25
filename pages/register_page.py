import sys
sys.path.append('./utils/')
sys.path.append('./testdata/')
from locators import RegisterPageLocators
from base_methods import BaseMethods
from logger import Logger




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
    
    def register(self, request, username, email, password):
        self.input_username(username)
        Logger.add_to_log(request).debug("Input username")
        self.input_email(email)
        Logger.add_to_log(request).debug("Input email")
        self.input_password(password)
        Logger.add_to_log(request).debug("Input password")
        self.click_create_account()
        Logger.add_to_log(request).debug("Click create account")
        