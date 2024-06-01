from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProjectPage():
    name_field = (By.ID, "name")
    prefix_field = (By.ID, "prefix")
    description_field = (By.ID, "description")
    save_button = (By.CSS_SELECTOR, "span#save")
    projects_icon = (By.CLASS_NAME, "activeMenu")

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def fill_projects_fields(self, project_name, prefix, description):
        self.browser.find_element(*self.name_field).send_keys(project_name)
        self.browser.find_element(*self.prefix_field).send_keys(prefix)
        self.browser.find_element(*self.description_field).send_keys(description)
        self.browser.find_element(*self.save_button).click()

    def click_projects_icon(self):
        self.wait.until(EC.element_to_be_clickable(self.projects_icon)).click()
        from pages.admin_panel_page import AdminPanelPage
        return AdminPanelPage(self.browser)
