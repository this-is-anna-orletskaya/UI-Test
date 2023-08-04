import pytest
import allure
import sys
sys.path.append('./pages/')
sys.path.append('./testdata/')
sys.path.append('./utils/')
from register_page import RegisterPage
from login_page import LoginPage
from main_page import MainPage
from projects_page import ProjectsPage
from labels_page import LabelsPage
from settings_page import SettingsPage
from tasks_page import TasksPage
from users import DefaultUser, ShortUser, WrongUser
from logger import Logger
from database import DbClient





"""Тестирование регистрации пользователя в системе"""
@allure.epic("Тестирование регистрации пользователя в системе")
@pytest.mark.usefixtures("setup")
class TestRegister:

    @pytest.fixture(autouse=True)
    def load_url(self, setup, request):
        Logger.add_to_log(request).info("Test started")
        self.register_page = RegisterPage(self.driver)
        self.register_page.load()
        Logger.add_to_log(request).debug("Loading register page")

    @allure.story("Тест регистрации нового пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("id, username, email, password", [(DefaultUser.id, DefaultUser.username, DefaultUser.email, DefaultUser.password), (ShortUser.id, ShortUser.username, ShortUser.email, ShortUser.password),])
    @pytest.mark.skip
    def test_register_new_user(self, request, id, username, email, password):
        
        rp = RegisterPage(self.driver)
        Logger.add_to_log(request).info(f"Input user data: {username, email, password}")
        rp.input_username(username) 
        Logger.add_to_log(request).debug("Input username")
        rp.input_email(email)
        Logger.add_to_log(request).debug("Input email")
        rp.input_password(password)
        Logger.add_to_log(request).debug("Input password")
        rp.click_create_account()
        Logger.add_to_log(request).debug("Create account")  

        mp = MainPage(self.driver) 
        Logger.add_to_log(request).info("Start checks by URL and title")
        mp.assert_text_element(mp.check_title(), "Текущие задачи")
        Logger.add_to_log(request).debug("Title is ok")
        mp.assert_url("https://try.vikunja.io/")
        Logger.add_to_log(request).debug("URL is ok")
        mp.save_screenshot()
        Logger.add_to_log(request).info("Checks passed successfully")
        assert DbClient.execute_read_query(f"SELECT * FROM vikunja.user WHERE username = '{username}'") == (id, username, password, email)


    @allure.story("Тест регистрации нового пользователя с использованием данных уже существующего пользователя")  
    @allure.severity(allure.severity_level.CRITICAL)
    def test_register_not_new_user(self, request):

        rp = RegisterPage(self.driver)
        Logger.add_to_log(request).info(f"Input user data: {DefaultUser.username, DefaultUser.password}")
        rp.register(request, DefaultUser.username, DefaultUser.email, DefaultUser.password)
        Logger.add_to_log(request).info("Start checks by message and URL")
        rp.assert_url("https://try.vikunja.io/register")
        Logger.add_to_log(request).debug("URL is ok")
        rp.assert_text_element(rp.cheking_message(), "A user with this username already exists.")
        Logger.add_to_log(request).debug("Message is ok")
        rp.save_screenshot()
        Logger.add_to_log(request).info("Checks passed successfully")



"""Тестирование авторизации в системе"""
@allure.epic("Тестирование авторизации в системе")
@pytest.mark.usefixtures("setup")
class TestLogin:

    @pytest.fixture(autouse=True)
    def load_url(self, setup, request):
        Logger.add_to_log(request).info("Test started")
        self.login_page = LoginPage(self.driver)
        self.login_page.load()
        Logger.add_to_log(request).debug("Loading login page")
    
    @allure.story("Тест авторизации пользователя")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login(self, request):

        lp = LoginPage(self.driver)
        Logger.add_to_log(request).info(f"Input user data: {DefaultUser.username, DefaultUser.password}")
        lp.log_in(request, DefaultUser.username, DefaultUser.password)

        mp = MainPage(self.driver)
        Logger.add_to_log(request).info("Start checks by title and URL")
        lp.assert_text_element(mp.check_title(), "Текущие задачи")
        Logger.add_to_log(request).debug("Title is ok")
        lp.assert_url("https://try.vikunja.io/")
        Logger.add_to_log(request).debug("URL is ok")
        mp.save_screenshot()
        Logger.add_to_log(request).info("Checks passed successfully")
    

    @allure.story("Тест авторизации пользователя с неправильными логином и паролем")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_wrong_user(self, request):

        lp = LoginPage(self.driver)
        Logger.add_to_log(request).info(f"Input user data: {WrongUser.username, WrongUser.password}")
        lp.log_in(request, WrongUser.username, WrongUser.password)
        Logger.add_to_log(request).info("Start checks by URL and message")
        lp.assert_url("https://try.vikunja.io/login")
        Logger.add_to_log(request).debug("URL is ok")
        lp.assert_text_element(lp.check_danger_message(), "Неверное имя пользователя или пароль.")
        Logger.add_to_log(request).debug("Message is ok")
        lp.save_screenshot()
        Logger.add_to_log(request).info("Checks passed successfully")



"""Тестирование функциональности"""
@allure.epic("Тестирование основной функциональности")
@pytest.mark.usefixtures("setup")
class TestBase:

    @pytest.fixture(autouse=True)
    def load_url(self, setup, request):
        Logger.add_to_log(request).info("Test started")
        self.login_page = LoginPage(self.driver)
        self.login_page.load()
        Logger.add_to_log(request).debug("Loading login page")

    @allure.story("Тест критического пути пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_critical_user_path(self, request):

        lp = LoginPage(self.driver)
        Logger.add_to_log(request).info(f"Input user data: {DefaultUser.username, DefaultUser.password}")
        with allure.step("Вход в систему"):
            lp.log_in(request, DefaultUser.username, DefaultUser.password)

        mp = MainPage(self.driver)
        Logger.add_to_log(request).info("Start checks by URL and title")
        mp.assert_text_element(mp.check_title(), "Текущие задачи")
        Logger.add_to_log(request).debug("Title is ok")
        mp.assert_url("https://try.vikunja.io/")
        Logger.add_to_log(request).debug("URL is ok")
        with allure.step("Переход к проектам"):
            mp.click_projects()
        Logger.add_to_log(request).debug("Click to projects")

        pp = ProjectsPage(self.driver)
        Logger.add_to_log(request).info(f"Creating project with name: {DefaultUser.project_name}")
        with allure.step("Создание проекта"):
            pp.create_project(request, DefaultUser.project_name)
        pp.assert_text_element(pp.check_project_title(), DefaultUser.project_name)
        Logger.add_to_log(request).debug("Project name is ok")
        Logger.add_to_log(request).info("Create task and click to checkbox")
        with allure.step("Добавление задачи и отметка о выполнении"):
            pp.add_task_click_checkbox(request, DefaultUser.task_name)
        pp.save_screenshot()
        Logger.add_to_log(request).info("Delete project")
        with allure.step("Удаление проекта"):
            pp.delete_project(request)
        pp.save_screenshot()

        mp = MainPage(self.driver)
        mp.assert_text_element(mp.check_title(), "Текущие задачи")
        Logger.add_to_log(request).debug("Title is ok")
        mp.assert_url("https://try.vikunja.io/")
        Logger.add_to_log(request).debug("URL is ok")
        with allure.step("Переход к меткам"):
            pp.click_labels()
        Logger.add_to_log(request).debug("Click to labels")

        lbp = LabelsPage(self.driver)
        Logger.add_to_log(request).info("Creating label")
        with allure.step("Создание метки"):
            lbp.create_label(request, DefaultUser.label1_name)
        lbp.save_screenshot()
        with allure.step("Переход к задачам"):
            lbp.click_upcoming_tasks()
        Logger.add_to_log(request).debug("Click to upcoming tasks")

        tp = TasksPage(self.driver)
        Logger.add_to_log(request).info("Select date interval")
        with allure.step("Выбор интервала дат: эта неделя"):
            tp.select_date_interval(request)
        with allure.step("Клик на чекбокс"):
            tp.click_checkbox()
        Logger.add_to_log(request).debug("Click checkbox")
        tp.save_screenshot()
        tp.assert_text_element(tp.check_title(), "Эта неделя")
        Logger.add_to_log(request).debug("Title is ok")
        with allure.step("Выход из системы"):
            tp.log_out(request)
        Logger.add_to_log(request).info("Click logout")
        tp.save_screenshot()

        lp = LoginPage(self.driver)
        lp.assert_text_element(lp.check_title(), "Войти")
        Logger.add_to_log(request).debug("Title is ok")
        Logger.add_to_log(request).info("Checks passed successfully")

    @allure.story("Тест создания проекта и задачи")    
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_project_add_task(self, request):

        lp = LoginPage(self.driver)
        Logger.add_to_log(request).info(f"Input user data: {DefaultUser.username, DefaultUser.password}")
        with allure.step("Вход в систему"):
            lp.log_in(request, DefaultUser.username, DefaultUser.password)

        mp = MainPage(self.driver)
        mp.assert_text_element(mp.check_title(), "Текущие задачи")
        Logger.add_to_log(request).debug("Title is ok")
        with allure.step("Переход к проектам"):
            mp.click_projects()
        Logger.add_to_log(request).debug("Click to projects")

        pp = ProjectsPage(self.driver)
        Logger.add_to_log(request).info(f"Creating project with name: {DefaultUser.project_name} and task: {DefaultUser.task_name}")
        with allure.step("Cоздание проекта и задачи в нем"):
            pp.create_project_add_task(request, DefaultUser.project_name, DefaultUser.task_name)
        Logger.add_to_log(request).info("Start check by project title")
        pp.assert_text_element(pp.check_project_title(), DefaultUser.project_name)
        Logger.add_to_log(request).debug(f"Project title '{DefaultUser.project_name}' is ok")
        pp.save_screenshot()
        Logger.add_to_log(request).info("Check passed successfully")
    
    @allure.story("Тест создания/удаления меток")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_delete_labels(self, request):
        
        lp = LoginPage(self.driver)
        Logger.add_to_log(request).info(f"Input user data: {DefaultUser.username, DefaultUser.password}")
        with allure.step("Вход в систему"):
            lp.log_in(request, DefaultUser.username, DefaultUser.password)

        mp = MainPage(self.driver)
        with allure.step("Переход к меткам"):
            mp.click_labels()
        Logger.add_to_log(request).debug("Click to labels")

        lbp = LabelsPage(self.driver)
        Logger.add_to_log(request).info("Creating labels")
        with allure.step("Создание первой метки"):
            lbp.create_label(request, DefaultUser.label1_name)
        with allure.step("Создание второй метки"):
            lbp.create_label(request, DefaultUser.label2_name)
        lbp.save_screenshot()

        Logger.add_to_log(request).info("Deleting label")
        with allure.step("Удаление метки"):
            lbp.click_delete_label()
        Logger.add_to_log(request).debug("Click delete label")
        with allure.step("Подтверждение удаления метки"):
            lbp.click_confirm_delete()
        Logger.add_to_log(request).debug("Click confirm delete label")
        lbp.save_screenshot()



"""Тестирвоание пользовательских настроек"""
@allure.epic("Тестирование пользовательских настроек")
@pytest.mark.usefixtures("setup")
class TestSettings:

    @pytest.fixture(autouse=True)
    def load_url(self, setup, request):
        Logger.add_to_log(request).info("Test started")
        self.login_page = LoginPage(self.driver)
        self.login_page.load()
        Logger.add_to_log(request).debug("Loading login page")
    
    @allure.story("Тест изменения пароля")
    @allure.issue("https://try.vikunja.io/user/settings/general", "500, internal server error")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="проблемы на стороне сервера")
    def test_change_password(self, request):
        
        lp = LoginPage(self.driver)
        Logger.add_to_log(request).info(f"Input user data: {DefaultUser.username, DefaultUser.password}")
        with allure.step("Вход в систему"):
            lp.log_in(request, DefaultUser.username, DefaultUser.password)

        mp = MainPage(self.driver)
        with allure.step("Переход в настройки"):
            mp.go_to_user_settings(request)
        Logger.add_to_log(request).debug("Click to user settings")

        sp = SettingsPage(self.driver)
        Logger.add_to_log(request).info("Changing password")
        with allure.step("Смена пароля"):
            sp.change_password(request, DefaultUser.new_password, DefaultUser.password)
        sp.save_screenshot()
        with allure.step("Выход из системы"):
            sp.log_out(request)
        Logger.add_to_log(request).info("Click logout")

        Logger.add_to_log(request).info(f"Login with username and new password: {DefaultUser.username, DefaultUser.new_password}")
        with allure.step("Вход в систему с новым паролем"):    
            lp.log_in(request, DefaultUser.username, DefaultUser.new_password)

        Logger.add_to_log(request).info("Start checks by URL and title")
        lp.assert_text_element(mp.check_title(), "Текущие задачи")
        Logger.add_to_log(request).debug("Title is ok")
        lp.assert_url("https://try.vikunja.io/")
        Logger.add_to_log(request).debug("URL is ok")
        lp.save_screenshot()
        Logger.add_to_log(request).info("Checks passed successfully")

