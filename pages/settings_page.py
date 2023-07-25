import sys
sys.path.append('./utils/')
sys.path.append('./testdata/')
from locators import SettingsPageLocators
from base_methods import BaseMethods
from logger import Logger




"""Страница настроек"""

class SettingsPage(BaseMethods):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    url = "https://try.vikunja.io/user/settings/general"

    def click_change_password(self):
        self.get_element_to_be_clickable_by_xpath(SettingsPageLocators.change_password_link_locator).click()

    def input_new_password(self, new_password):
        self.get_element_to_be_clickable_by_xpath(SettingsPageLocators.new_password_field_locator).send_keys(new_password)
    
    def input_new_password_again(self, new_password):
        self.get_element_to_be_clickable_by_xpath(SettingsPageLocators.confirm_new_password_field_locator).send_keys(new_password)
    
    def input_old_password(self, old_password):
        self.get_element_to_be_clickable_by_xpath(SettingsPageLocators.old_password_field_locator).send_keys(old_password)

    def click_save_password(self):
        self.get_element_to_be_clickable_by_xpath(SettingsPageLocators.save_button_locator).click()
    
    def click_username(self):
        self.get_element_to_be_clickable_by_xpath(SettingsPageLocators.username_button_locator).click()
    
    def click_log_out(self):
        self.get_element_to_be_clickable_by_xpath(SettingsPageLocators.log_out_button_locator).click()


    """Основные тестовые методы"""

    def change_password(self, request, new_password, old_password):
        self.click_change_password()
        Logger.add_to_log(request).debug("Click change password")
        self.input_new_password(new_password)
        Logger.add_to_log(request).debug("Input new password")
        self.input_new_password_again(new_password)
        Logger.add_to_log(request).debug("Input new password on second field")
        self.input_old_password(old_password)
        Logger.add_to_log(request).debug("Input old password")
        self.click_save_password()
        Logger.add_to_log(request).debug("Click save password")
    
    def log_out(self, request):
        self.click_username()
        Logger.add_to_log(request).debug("Click on username")
        self.click_log_out()
        Logger.add_to_log(request).debug("Click log out")