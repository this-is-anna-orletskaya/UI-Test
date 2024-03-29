import sys
sys.path.append('./utils/')
sys.path.append('./testdata/')
from locators import TasksPageLocators
from base_methods import BaseMethods
from logger import Logger



"""Страница с выбором задач"""

class TasksPage(BaseMethods):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    url = "https://try.vikunja.io/tasks/by/upcoming"

    def click_view(self):
        self.get_element_to_be_clickable(TasksPageLocators.view_link_locator).click()
        
    def click_upcoming_tasks(self):
        self.get_element_to_be_clickable(TasksPageLocators.upcoming_tasks_link_locator).click()
    
    def click_projects(self):
        self.get_element_to_be_clickable(TasksPageLocators.projects_link_locator).click()

    def click_labels(self):
        self.get_element_to_be_clickable(TasksPageLocators.labels_link_locator).click()

    def click_teams(self):
        self.get_element_to_be_clickable(TasksPageLocators.teams_link_locator).click()
    
    def click_username(self):
        self.get_element_to_be_clickable(TasksPageLocators.username_button_locator).click()

    def click_settings(self):
        self.get_element_to_be_clickable(TasksPageLocators.settings_button_locator).click()

    def click_log_out(self):
        self.get_element_to_be_clickable(TasksPageLocators.log_out_button_locator).click()
    
    def click_select_date(self):
        self.get_element_to_be_clickable(TasksPageLocators.select_date_button_locator).click()
    
    def click_this_week_interval(self):
        self.get_element_to_be_clickable(TasksPageLocators.this_week_interval_locator).click()
    
    def click_desktop(self):
        self.get_element_to_be_clickable(TasksPageLocators.desktop_locator).click()
    
    def click_checkbox(self):
        self.get_element_to_be_clickable(TasksPageLocators.checkbox_locator).click()
    
    def check_title(self):
        return self.get_element_to_be_clickable(TasksPageLocators.check_title_locator)
    
    def click_username(self):
        self.get_element_to_be_clickable(TasksPageLocators.username_button_locator).click()
    
    def click_log_out(self):
        self.get_element_to_be_clickable(TasksPageLocators.log_out_button_locator).click()
    

    """Основные тестовые методы"""

    def select_date_interval(self, request):
        self.click_select_date()
        Logger.add_to_log(request).debug("Click select date")
        self.click_this_week_interval()
        Logger.add_to_log(request).debug("Click choose this week interval")
        self.click_desktop()
        Logger.add_to_log(request).debug("Click on the desktop")

    def log_out(self, request):
        self.click_username()
        Logger.add_to_log(request).debug("Click on username")
        self.click_log_out()
        Logger.add_to_log(request).debug("Click log out")

