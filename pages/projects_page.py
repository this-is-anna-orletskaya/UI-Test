import sys
sys.path.append('./utils/')
sys.path.append('./testdata/')
from locators import ProjectsPageLocators
from base_methods import BaseMethods
from logger import Logger
from selenium.common.exceptions import StaleElementReferenceException




"""Страница проектов"""

class ProjectsPage(BaseMethods):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    url = "https://try.vikunja.io/projects"

    def click_view(self):
        self.get_element_to_be_clickable_by_xpath(ProjectsPageLocators.view_link_locator).click()
        
    def click_upcoming_tasks(self):
        self.get_element_to_be_clickable_by_xpath(ProjectsPageLocators.upcoming_tasks_link_locator).click()
    
    def click_projects(self):
        self.get_element_to_be_clickable_by_xpath(ProjectsPageLocators.projects_link_locator).click()

    def click_labels(self):
        self.get_element_to_be_clickable_by_xpath(ProjectsPageLocators.labels_link_locator).click()

    def click_teams(self):
        self.get_element_to_be_clickable_by_xpath(ProjectsPageLocators.teams_link_locator).click()

    def click_create_project(self):
        self.get_element_to_be_clickable_by_xpath(ProjectsPageLocators.create_project_button_locator).click()

    def input_project_name(self, name):
        self.get_element_to_be_clickable_by_xpath(ProjectsPageLocators.project_name_field_locator).send_keys(name)
    
    def click_create_button(self):
        self.get_element_to_be_clickable_by_xpath(ProjectsPageLocators.create_button_locator).click()

    def click_create_new_saved_filter(self):
        self.get_element_to_be_clickable_by_xpath(ProjectsPageLocators.create_new_saved_filter_button_locator).click()
    
    def input_taskname(self, taskname):
        self.get_element_to_be_clickable_by_xpath(ProjectsPageLocators.task_for_project_field_locator).send_keys(taskname)
    
    def click_add_task_button(self):
        self.get_element_to_be_clickable_by_xpath(ProjectsPageLocators.add_task_button_locator).click()
    
    def click_task_chexbox(self):
        self.get_element_to_be_clickable_by_xpath(ProjectsPageLocators.checkbox_locator).click()
    
    def click_project_menu(self):
        self.get_element_to_be_clickable_by_xpath(ProjectsPageLocators.project_menu_locator).click()
    
    def click_delete_project(self):
        self.get_element_to_be_clickable_by_xpath(ProjectsPageLocators.delete_project_locator).click()
    
    def click_confirm_delete_project(self):
        self.get_element_to_be_clickable_by_xpath(ProjectsPageLocators.confirm_delete_project_button_locator).click()

    def check_project_title(self):
        return self.get_element_to_be_clickable_by_xpath(ProjectsPageLocators.check_project_title_locator)

    
    """Основные тестовые методы"""

    def create_project(self, request, name):
        self.click_create_project()
        Logger.add_to_log(request).debug("Click create project")
        self.input_project_name(name)
        Logger.add_to_log(request).debug("Input project name")
        self.click_create_button()
        Logger.add_to_log(request).debug("Click create")
    
    def add_task_click_checkbox(self, request, taskname):
        self.input_taskname(taskname)
        Logger.add_to_log(request).debug("Input task name")
        self.click_add_task_button()
        Logger.add_to_log(request).debug("Click add task")
        self.click_task_chexbox()
        Logger.add_to_log(request).debug("Click checkbox")

    def create_project_add_task(self, request, name, taskname):
        self.click_create_project()
        Logger.add_to_log(request).debug("Click create project")
        self.input_project_name(name)
        Logger.add_to_log(request).debug("Input project name")
        self.click_create_button()
        Logger.add_to_log(request).debug("Click create")
        self.input_taskname(taskname)
        Logger.add_to_log(request).debug("Input task name")
        self.click_add_task_button()
        Logger.add_to_log(request).debug("Click add task")

    def delete_project(self, request):
        self.click_project_menu()
        Logger.add_to_log(request).debug("Click project menu")
        self.click_delete_project()
        Logger.add_to_log(request).debug("Click delete project")
        try:
            self.click_confirm_delete_project()
            Logger.add_to_log(request).debug("Click confirm delete project")
        except StaleElementReferenceException:
            Logger.add_to_log(request).exception("StaleElementReferenceException")
            self.click_confirm_delete_project()
            Logger.add_to_log(request).debug("Click confirm delete project")



    
