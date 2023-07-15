


"""Локаторы элементов на страницах"""

class RegisterPageLocators:

    username_field_locator = "//input[@id='username']"
    email_field_locator = "//input[@id='email']"
    password_field_locator = "//input[@id='password']"
    create_account_button_locator = "//button[@id='register-submit']"
    go_log_in_locator = "//a[@href='/login']"
    checking_message_locator = "//div[@class='message danger']"
    danger_message_locator = "//p[@class='help is-danger']"


class LoginPageLocators:

    username_field_locator = "//input[@id='username']"
    password_field_locator = "//input[@id='password']"
    remember_me_chekbox_locator =  "//input[@type='checkbox']"
    forgot_password_link_locator = "//a[@class='reset-password-link']"
    log_in_button_locator = "//button[@class='base-button base-button--type-button button is-primary']"
    go_register_link_locator = "//a[@href='/register']"
    check_title_locator = "//h2[@class='title']"

class MainPageLocators:

    """Боковое меню"""
    view_link_locator = "//a[@href='/']"
    upcoming_tasks_link_locator = "//a[@href='/tasks/by/upcoming']"
    projects_link_locator = "//a[@href='/projects']"
    labels_link_locator = "//a[@href='/labels']"
    teams_link_locator = "//a[@href='/teams']"

    """Меню пользователя"""
    username_button_locator = "//button[@class='base-button base-button--type-button username-dropdown-trigger']"
    settings_button_locator = "//a[@href='/user/settings']"
    log_out_button_locator = "//button[@type='button'][@class='base-button base-button--type-button dropdown-item'][2]"

    """Центральная панель"""
    task_field_locator = "//textarea[@class='add-task-textarea input textarea-empty']"
    task_button_locator = "//button[@class='base-button base-button--type-button button is-primary add-task-button']"
    check_title_locator = "//h3[@class='mb-2 title']"


class ProjectsPageLocators:

    """Боковое меню"""
    view_link_locator = "//a[@href='/']"
    upcoming_tasks_link_locator = "//a[@href='/tasks/by/upcoming']"
    projects_link_locator = "//a[@href='/projects']"
    labels_link_locator = "//a[@href='/labels']"
    teams_link_locator = "//a[@href='/teams']"

    """Меню пользователя"""
    username_button_locator = "//button[@class='base-button base-button--type-button username-dropdown-trigger']"
    settings_button_locator = "//a[@href='/user/settings']"
    log_out_button_locator = "//button[@type='button'][@class='base-button base-button--type-button dropdown-item'][2]"

    """Центральная панель"""
    create_project_button_locator = "//a[@href='/projects/new']"
    create_new_saved_filter_button_locator = "//a[@href='/filters/new']"
    project_name_field_locator = "//input[@name='projectTitle']"
    parent_project_field_locator = "//div[@class='input-wrapper input']"
    create_button_locator = "//button[@class='base-button base-button--type-button button is-primary ml-2']"
    task_for_project_field_locator = "//textarea[@class='add-task-textarea input textarea-empty']"
    add_task_button_locator = "//button[@class='base-button base-button--type-button button is-primary add-task-button']"
    checkbox_locator = "//label[@class='base-checkbox__label']"
    project_menu_locator = "//button[@class='base-button base-button--type-button project-title-button']"
    delete_project_locator = "//a[@class='base-button dropdown-item has-text-danger']"
    confirm_delete_project_button_locator = "//button[@class='base-button base-button--type-button button is-primary has-no-shadow']"
    check_project_title_locator = "//h1[@class='project-title']"


class LabelsPageLocators:

    """Боковое меню"""
    view_link_locator = "//a[@href='/']"
    upcoming_tasks_link_locator = "//a[@href='/tasks/by/upcoming']"
    projects_link_locator = "//a[@href='/projects']"
    labels_link_locator = "//a[@href='/labels']"
    teams_link_locator = "//a[@href='/teams']"

    """Меню пользователя"""
    username_button_locator = "//button[@class='base-button base-button--type-button username-dropdown-trigger']"
    settings_button_locator = "//a[@href='/user/settings']"
    log_out_button_locator = "//button[@type='button'][@class='base-button base-button--type-button dropdown-item'][2]"

    """Центральная панель"""
    new_label_button_locator = "//a[@href='/labels/new']"
    label_field_locator = "//input[@id='labelTitle']"
    create_button_locator = "//button[@class='base-button base-button--type-button button is-primary ml-2']"
    delete_label_button_locator = "//button[@class='base-button base-button--type-button delete is-small']"
    confirm_delete_button_locator = "//button[@class='base-button base-button--type-button button is-primary has-no-shadow']"
    check_label_locator = "//span[@class='tag']"


class SettingsPageLocators:

    """Боковое меню"""
    view_link_locator = "//a[@href='/']"
    upcoming_tasks_link_locator = "//a[@href='/tasks/by/upcoming']"
    projects_link_locator = "//a[@href='/projects']"
    labels_link_locator = "//a[@href='/labels']"
    teams_link_locator = "//a[@href='/teams']"

    """Меню пользователя"""
    username_button_locator = "//button[@class='base-button base-button--type-button username-dropdown-trigger']"
    settings_button_locator = "//a[@href='/user/settings']"
    log_out_button_locator = "//button[@type='button'][@class='base-button base-button--type-button dropdown-item'][2]"
    
    """Центральная панель"""
    change_password_link_locator = "//a[@href='/user/settings/password-update']"
    new_password_field_locator = "//input[@id='newPassword']"
    confirm_new_password_field_locator = "//input[@id='newPasswordConfirm']"
    old_password_field_locator = "//input[@id='currentPassword']"
    save_button_locator = "//button[@class='base-button base-button--type-button button is-primary is-fullwidth mt-4']"


class TasksPageLocators:

    """Боковое меню"""
    view_link_locator = "//a[@href='/']"
    upcoming_tasks_link_locator = "//a[@href='/tasks/by/upcoming']"
    projects_link_locator = "//a[@href='/projects']"
    labels_link_locator = "//a[@href='/labels']"
    teams_link_locator = "//a[@href='/teams']"

    """Меню пользователя"""
    username_button_locator = "//button[@class='base-button base-button--type-button username-dropdown-trigger']"
    settings_button_locator = "//a[@href='/user/settings']"
    log_out_button_locator = "//button[@type='button'][@class='base-button base-button--type-button dropdown-item'][2]"

    """Центральная панель"""
    select_date_button_locator = "//button[@class='base-button base-button--type-button button is-primary has-no-shadow mb-2']"
    this_week_interval_locator = "//button[@class='base-button base-button--type-button'][3]"
    desktop_locator = "//div[@class='is-max-width-desktop has-text-left']"
    checkbox_locator = "//span[@class='fancycheckbox__content'][1]"
    check_title_locator = "//h3[@class='mb-2 title']"
