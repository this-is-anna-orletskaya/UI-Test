import sys
sys.path.append('./utils/')
sys.path.append('./testdata/')
from locators import MainPageLocators
from base_methods import BaseMethods
from logger import Logger




"""Основная страница"""

class MainPage(BaseMethods):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = "https://try.vikunja.io/"

    def click_view(self):
        self.get_element_to_be_clickable_by_xpath(MainPageLocators.view_link_locator).click()
        
    def click_upcoming_tasks(self):
        self.get_element_to_be_clickable_by_xpath(MainPageLocators.upcoming_tasks_link_locator).click()
    
    def click_projects(self):
        self.get_element_to_be_clickable_by_xpath(MainPageLocators.projects_link_locator).click()

    def click_labels(self):
        self.get_element_to_be_clickable_by_xpath(MainPageLocators.labels_link_locator).click()

    def click_teams(self):
        self.get_element_to_be_clickable_by_xpath(MainPageLocators.teams_link_locator).click()
    
    def click_username(self):
        self.get_element_to_be_clickable_by_xpath(MainPageLocators.username_button_locator).click()

    def click_settings(self):
        self.get_element_to_be_clickable_by_xpath(MainPageLocators.settings_button_locator).click()

    def click_log_out(self):
        self.get_element_to_be_clickable_by_xpath(MainPageLocators.log_out_button_locator).click()

    def input_task_field(self, task):
        self.get_element_to_be_clickable_by_xpath(MainPageLocators.task_field_locator).send_keys(task)

    def click_task_button(self):
        self.get_element_to_be_clickable_by_xpath(MainPageLocators.task_button_locator).click()
    
    def check_title(self):
        return self.get_element_to_be_clickable_by_xpath(MainPageLocators.check_title_locator)

    
    """Основные тестовые методы"""

    def create_task(self, request, task):
        self.input_task_field(task)
        Logger.add_to_log(request).debug("Input task")
        self.click_task_button()
        Logger.add_to_log(request).debug("Click create task")
    
    def go_to_user_settings(self, request):
        self.click_username()
        Logger.add_to_log(request).debug("Click on username")
        self.click_settings()
        Logger.add_to_log(request).debug("Click on settings")