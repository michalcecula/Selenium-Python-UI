from fixtures.chrome import chrome_browser
from fixtures.testarena.login import browser
from pages import admin_panel_page
from pages.admin_panel_page import AdminPanelPage
from pages.home_page import HomePage
from pages.projects_page import ProjectPage

project_name = "Projekt 2055"
prefix = "2055"
description = "Program 2055"


def test_new_project(browser):
    home_page = HomePage(browser)
    admin_panel_page = home_page.click_admin_panel()

    projects_page = admin_panel_page.click_add_project_button()
    projects_page.fill_projects_fields(project_name, prefix, description)

    admin_panel_page = projects_page.click_projects_icon()
    admin_panel_page.search_project(project_name)

    assert admin_panel_page.verify_project_exist(project_name)
