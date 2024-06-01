from fixtures.chrome import chrome_browser
from fixtures.testarena.login import browser
from pages.home_page import HomePage
import string
import random


def generate_random_string(length=10):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


project_name = generate_random_string()
prefix = generate_random_string()
description = generate_random_string()


def test_new_project(browser):
    home_page = HomePage(browser)
    admin_panel_page = home_page.click_admin_panel()
    projects_page = admin_panel_page.click_add_project_button()
    projects_page.fill_projects_fields(project_name, prefix, description)
    admin_panel_page = projects_page.click_projects_icon()
    admin_panel_page.search_project(project_name)

    assert admin_panel_page.verify_project_exist(project_name)
