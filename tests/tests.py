import pytest
import sys
sys.path.append('./pages/')
sys.path.append('./testdata/')
from register_page import RegisterPage
from login_page import LoginPage
from main_page import MainPage
from projects_page import ProjectsPage
from labels_page import LabelsPage
from settings_page import SettingsPage
from tasks_page import TasksPage
from users import DefaultUser, ShortUser, WrongUser
from assertions import Assertions




"""Тестирование регистрации пользователя в системе"""
@pytest.mark.usefixtures("setup")
class TestRegister:

    @pytest.fixture(autouse=True)
    def load_url(self, setup):
        self.register_page = RegisterPage(self.driver)
        self.register_page.load()


    @pytest.mark.parametrize("username, email, password", [(DefaultUser.username, DefaultUser.email, DefaultUser.password), (ShortUser.username, ShortUser.email, ShortUser.password),])
    def test_register_new_user(self, username, email, password):

        rp = RegisterPage(self.driver)
        rp.input_username(username) 
        rp.input_email(email)
        rp.input_password(password)
        rp.click_create_account()  

        mp = MainPage(self.driver) 

        Assertions.check_word(mp.check_title(), "Текущие задачи")
        Assertions.assert_url(self.driver, "https://try.vikunja.io/")
        rp.save_screenshot()
        

    def test_register_not_new_user(self):
        rp = RegisterPage(self.driver)
        try:
            rp.register(DefaultUser.username, DefaultUser.email, DefaultUser.password)
            Assertions.assert_url(self.driver, "https://try.vikunja.io/register")
            Assertions.check_word(rp.cheking_message(), "A user with this username already exists.")
        except AssertionError:
            rp.register(DefaultUser.username, DefaultUser.email, DefaultUser.password)
            Assertions.check_word(rp.cheking_message(), "A user with this username already exists.")
            Assertions.assert_url(self.driver, "https://try.vikunja.io/register")
        finally:
            rp.save_screenshot()



"""Тестирование авторизации в системе"""
@pytest.mark.usefixtures("setup")
class TestLogin:

    @pytest.fixture(autouse=True)
    def load_url(self, setup):
        self.login_page = LoginPage(self.driver)
        self.login_page.load()


    def test_login(self):

        lp = LoginPage(self.driver)
        lp.log_in(DefaultUser.username, DefaultUser.password)
        
        mp = MainPage(self.driver)
        mp.save_screenshot()
        Assertions.assert_url(self.driver, "https://try.vikunja.io/")
        Assertions.check_word(mp.check_title(), "Текущие задачи")
    

    def test_login_wrong_user(self):

        lp = LoginPage(self.driver)
        lp.log_in(WrongUser.username, WrongUser.password)
        Assertions.assert_url(self.driver, "https://try.vikunja.io/login")
        Assertions.check_word(lp.check_danger_message(), "Неверное имя пользователя или пароль.")
        lp.save_screenshot()



"""Тестирование функциональности"""
@pytest.mark.usefixtures("setup")
class TestBase:

    @pytest.fixture(autouse=True)
    def load_url(self, setup):
        self.login_page = LoginPage(self.driver)
        self.login_page.load()


    def test_critical_user_path(self):

        lp = LoginPage(self.driver)
        lp.log_in(DefaultUser.username, DefaultUser.password)

        mp = MainPage(self.driver)
        Assertions.check_word(mp.check_title(), "Текущие задачи")
        Assertions.assert_url(self.driver, "https://try.vikunja.io/")
        mp.click_projects()

        pp = ProjectsPage(self.driver)
        pp.create_project(DefaultUser.project_name)
        Assertions.check_word(pp.check_project_title(), DefaultUser.project_name)
        pp.add_task_click_checkbox(DefaultUser.task_name)
        pp.save_screenshot()
        pp.delete_project()
        pp.save_screenshot()

        mp = MainPage(self.driver)
        Assertions.check_word(mp.check_title(), "Текущие задачи")
        Assertions.assert_url(self.driver, "https://try.vikunja.io/")
        pp.click_labels()

        lbp = LabelsPage(self.driver)
        lbp.create_label(DefaultUser.label1_name)
        lbp.save_screenshot()
        lbp.click_upcoming_tasks()

        tp = TasksPage(self.driver)
        tp.select_date_interval()
        tp.click_checkbox()
        tp.save_screenshot()
        Assertions.check_word(tp.check_title(), "Эта неделя")
        tp.click_username()
        tp.click_log_out()
        tp.save_screenshot()

        lp = LoginPage(self.driver)
        Assertions.check_word(lp.check_title(), "Войти")
        

    def test_create_project_add_task(self):

        lp = LoginPage(self.driver)
        lp.log_in(DefaultUser.username, DefaultUser.password)

        mp = MainPage(self.driver)
        Assertions.check_word(mp.check_title(), "Текущие задачи")
        Assertions.assert_url(self.driver, "https://try.vikunja.io/")
        mp.click_projects()

        pp = ProjectsPage(self.driver)
        pp.create_project_add_task(DefaultUser.project_name, DefaultUser.task_name)
        Assertions.check_word(pp.check_project_title(), DefaultUser.project_name)
        pp.save_screenshot()
    

    def test_create_delete_labels(self):
        
        lp = LoginPage(self.driver)
        lp.log_in(DefaultUser.username, DefaultUser.password)

        mp = MainPage(self.driver)
        mp.click_labels()

        lbp = LabelsPage(self.driver)
        lbp.create_label(DefaultUser.label1_name)
        lbp.create_label(DefaultUser.label2_name)
        lbp.save_screenshot()
        lbp.click_delete_label()
        lbp.click_confirm_delete()
        lbp.save_screenshot()



"""Тестирвоание пользовательских настроек"""
@pytest.mark.usefixtures("setup")
class TestSettings:

    @pytest.fixture(autouse=True)
    def load_url(self, setup):
        self.login_page = LoginPage(self.driver)
        self.login_page.load()
    

    @pytest.mark.xfail(reason="проблемы на стороне сервера")
    def test_change_password(self):

        lp = LoginPage(self.driver)
        lp.log_in(DefaultUser.username, DefaultUser.password)

        mp = MainPage(self.driver)
        mp.go_to_user_settings()

        sp = SettingsPage(self.driver)
        sp.change_password(DefaultUser.new_password, DefaultUser.password)
        sp.save_screenshot()
        sp.log_out()

        lp.log_in(DefaultUser.username, DefaultUser.new_password)
        lp.save_screenshot()

        Assertions.check_word(mp.check_title(), "Текущие задачи")
        Assertions.assert_url(self.driver, "https://try.vikunja.io/")
