import sys
sys.path.append('./utils/')
sys.path.append('./testdata/')
from locators import TasksPageLocators
from base_methods import BaseMethods





"""Страница регистрации на сайте"""

class TasksPage(BaseMethods):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    url = "https://try.vikunja.io/tasks/by/upcoming"

    def click_view(self):
        self.get_element_to_be_clickable_by_xpath(TasksPageLocators.view_link_locator).click()
        
    def click_upcoming_tasks(self):
        self.get_element_to_be_clickable_by_xpath(TasksPageLocators.upcoming_tasks_link_locator).click()
    
    def click_projects(self):
        self.get_element_to_be_clickable_by_xpath(TasksPageLocators.projects_link_locator).click()

    def click_labels(self):
        self.get_element_to_be_clickable_by_xpath(TasksPageLocators.labels_link_locator).click()

    def click_teams(self):
        self.get_element_to_be_clickable_by_xpath(TasksPageLocators.teams_link_locator).click()
    
    def click_username(self):
        self.get_element_to_be_clickable_by_xpath(TasksPageLocators.username_button_locator).click()

    def click_settings(self):
        self.get_element_to_be_clickable_by_xpath(TasksPageLocators.settings_button_locator).click()

    def click_log_out(self):
        self.get_element_to_be_clickable_by_xpath(TasksPageLocators.log_out_button_locator).click()
    
    def click_select_date(self):
        self.get_element_to_be_clickable_by_xpath(TasksPageLocators.select_date_button_locator).click()
    
    def click_this_week_interval(self):
        self.get_element_to_be_clickable_by_xpath(TasksPageLocators.this_week_interval_locator).click()
    
    def click_desktop(self):
        self.get_element_to_be_clickable_by_xpath(TasksPageLocators.desktop_locator).click()
    
    def click_checkbox(self):
        self.get_element_to_be_clickable_by_xpath(TasksPageLocators.checkbox_locator).click()
    
    def check_title(self):
        return self.get_element_to_be_clickable_by_xpath(TasksPageLocators.check_title_locator)
    

    """Основные тестовые методы"""

    def select_date_interval(self):
        self.click_select_date()
        self.click_this_week_interval()
        self.click_desktop()

