import sys
sys.path.append('./utils/')
sys.path.append('./testdata/')
from locators import LabelsPageLocators
from base_methods import BaseMethods
from logger import Logger



"""Страница проектов"""

class LabelsPage(BaseMethods):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    url = "https://try.vikunja.io/projects"

    def click_view(self):
        self.get_element_to_be_clickable(LabelsPageLocators.view_link_locator).click()
        
    def click_upcoming_tasks(self):
        self.get_element_to_be_clickable(LabelsPageLocators.upcoming_tasks_link_locator).click()
    
    def click_projects(self):
        self.get_element_to_be_clickable(LabelsPageLocators.projects_link_locator).click()

    def click_labels(self):
        self.get_element_to_be_clickable(LabelsPageLocators.labels_link_locator).click()

    def click_teams(self):
        self.get_element_to_be_clickable(LabelsPageLocators.teams_link_locator).click()

    def click_new_label(self):
        self.get_element_to_be_clickable(LabelsPageLocators.new_label_button_locator).click()

    def input_label_name(self, name):
        self.get_element_to_be_clickable(LabelsPageLocators.label_field_locator).send_keys(name)

    def click_create_label(self):
        self.get_element_to_be_clickable(LabelsPageLocators.create_button_locator).click()
    
    def click_delete_label(self):
        self.get_element_to_be_clickable(LabelsPageLocators.delete_label_button_locator).click()
    
    def click_confirm_delete(self):
        self.get_element_to_be_clickable(LabelsPageLocators.confirm_delete_button_locator).click()
    
    def check_label_name(self):
        return self.get_element_is_visible(LabelsPageLocators.check_label_locator).click()


    """Основные тестовые методы"""

    def create_label(self, request, name):
        self.click_new_label()
        Logger.add_to_log(request).debug("Click create new label")
        self.input_label_name(name)
        Logger.add_to_log(request).debug("Input label name")
        self.click_create_label()
        Logger.add_to_log(request).debug("Click create label")
    
    def delete_label(self, request):
        self.click_delete_label()
        Logger.add_to_log(request).debug("Click delete label")
        self.click_confirm_delete()
        Logger.add_to_log(request).debug("Click confirm delete label")
    
